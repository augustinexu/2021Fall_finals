import pandas as pd
import numpy as np
import plotly as py
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import ipywidgets
import bqplot
from bqplot import pyplot
from bqplot import Tooltip

def world_data()->None:
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")
    df.fillna(value=0, inplace=True)
    date = df.date.str.split('-', expand=True)
    df['year'] = date[0]
    df['month'] = date[1]
    df['day'] = date[2]
    df.year = pd.to_numeric(df.year)
    df.month = pd.to_numeric(df.month)
    df.day = pd.to_numeric(df.day)
    df.date = pd.to_datetime(df.date)

def min_max(df)->None:
    numeric_col = df[
        ['location', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'total_boosters',
         'daily_vaccinations_raw',
         'daily_vaccinations', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
         'people_fully_vaccinated_per_hundred'
            , 'total_boosters_per_hundred', 'daily_vaccinations_per_million', 'daily_people_vaccinated',
         'daily_people_vaccinated_per_hundred']]
    vac_mean = numeric_col.groupby('location').mean().round(0)
    vac_sum = numeric_col.groupby('location').sum()
    vac_mean.min()
    vac_mean.max()
    vac_sum.min()
    vac_sum.max()


def data_to_color(map_data,vac_mean):
    name = []
    for i in map_data:
        name.append((i['properties']['name'],i['id']))
    name = dict(name)
    color = []
    for name, idx in name.items():
        daily_vac_mean = vac_mean[vac_mean.index.str.contains(name)].total_vaccinations.values
        if len(daily_vac_mean) > 0:
            color.append((idx, daily_vac_mean[0]))
    return dict(color)

def plot_global_vacc()->None:
    fig = pyplot.figure(title='Global average daily vaccination')
    pyplot.scales(scales={'color': bqplot.ColorScale(scheme='RdYlBu')})
    world_map = pyplot.geo(map_data='WorldMap',
                           colors={'default_color': 'Grey'})
    map_data = world_map.map_data['objects']['subunits']['geometries']
    world_map.color = data_to_color(map_data)
    world_map.tooltip = Tooltip(fields=['color'], labels=['Daily average vaccinations'])
    fig
    pyplot.show()

def daily_dynamic_plot(df):
    plt.figure(figsize=(16, 8))
    sns.lineplot(x=df.date, y=df.daily_vaccinations)
    plt.title('The Number of daily vaccinations dynamic')
    plt.show()

def procedure_plot(df):
    countries = df.groupby('location')['total_vaccinations'].max().sort_values(ascending=False)[:5].index

    top_countries = pd.DataFrame(columns=df.columns)
    for country in countries:
        top_countries = top_countries.append(df.loc[df['location'] == country])
    plt.figure(figsize=(20, 8))
    sns.lineplot(top_countries['date'], top_countries['daily_vaccinations_per_million'],
                     hue=top_countries['location'], ci=False)
    plt.title('Vaccination procedure go on rapidly');

def ():
    location = df.location.unique()
    vaccination_subset = df.loc[((df.location == 'Zambia') & (df.people_fully_vaccinated != 0))]  # ["Zambia"]
    vaccination_subset