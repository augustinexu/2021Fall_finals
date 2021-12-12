# COVID-19 Vaccination Data Analysis（Type I）
Group Members: Qianqian Wang(GithubID: wangqianqian122), Augustine Xu(GithubID: augustinexu)

## Backgroud
Since December 2019, a number of pneumonia cases of unknown cause with a history of exposure to seafood markets in South China have been detected in some hospitals in Wuhan, Hubei Province. This desease has been confirmed as acute respiratory infections caused by Novel Coronavirus infection and is named as Covid-19. Covid-19 is a serious infectious disease which already has impacted many countries and threat many people’s health. It makes people get fever, cough, shortness of breath and even loss of taste or smell. Since the virus cannot be defended against by people's own resistance, vaccine is necessary for everyone. Our group choose the analysis report 'COVID-19 Vaccination Data Analysis' from Kaggle.com. This project is about "COVID-19 World Vaccination Progress" Data Analysis with Python. We try to improve the quality of this report and extend the content of it.

## Link of the Analysis
https://www.kaggle.com/anirbansahaanik/covid-19-vaccination-data-analysis/notebook

## Datasets
1.kaggle kernels output anirbansahaanik/covid-19-vaccination-data-analysis -p /path/to/dest

2.https://data.cdc.gov/Vaccinations/COVID-19-Vaccination-Demographics-in-the-United-St/km4m-vcsb

3.https://github.com/owid/covid-19-data

4.https://www2.census.gov/geo/docs/reference/ua

5.https://worldpopulationreview.com/state-rankings/per-capita-income-by-state

## Content of the Original Analysis
- Data Preprocessing: Spliting date to year, month, day; Replacing all NaN Value to 0 
- Exploratory Analysis and Visualization:
  Primary Data: mean, min, max of the dataset;  min and max of people_fully_vaccinated and date
  Two charts: The Number of daily vaccinations dynamic,  Vaccination procedure go on
- Questions
1. Which country has most number of fully vaccinated people?  
2. Daily COVID-19 vaccine doses administered per million people.
3. How many people daily vaccinated in Bangladesh?
4. How many people take at least one dose of vaccine in Bangladesh?
5. What is the country that vaccinated completely most of the population?

## Questions and Improvements
### 1. Problem On Exploratory Analysis 
The author tried to show the overall situation of this dataset by primary data of it such as minimun of total_vaccinaions, people_vaccinated and so on. However, as the follwing picture showing, all data is 0. In the preprocessing, all NaN values are replaced as 0, so the value of minimun must be 0. By this method of preprocessing, the part of minimun is useless to express any important Information.

<div align=center><img width = "600" height= "400" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/minimun.png/></div>

### Improvement On Exploratory Analysis 
Our group create two new charts to show the situation of the vacciantion. The first chart shows the Global Average Daily Vaccination in a geometric map. The second one shows The Number of Fully Vaccinated in each country by using dropdown.
<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Global%20Average%20Daily%20Vaccination.png/></div>
<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/each_country.png/></div>

### 2. Problem On Question Three
Question Three is 'How many people daily vaccinated in Bangladesh?'.
For showing more information about Bangladesh, the analysis report uses line chart to show the number daily vaccinated people each day. However, there are too many days which have no data, and the data of those days maybe calculated in the later day. As a result, line chart is not suitable to show the situation of vaccinated people in Bangladesh, and it is not good to show the data of each day.  
<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Bangladesh.png/></div>

### Improvement On Question Four
We change the type of chart to bar charts. For the first bar chart,  the time interval has been settled as month. For the second one, there is a downdrop to choose the specific month, and it shows daily vaccinated people each day of this month.
<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Daily%20Vaccinated%20in%20Bangladesh.png/></div>

<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Daily%20Vaccination%20of%20each%20month.png/></div>

### 3. Problem On Question4
Question Four is 'How many people take at least one dose of vaccine in Bangladesh?'.
The original analysis use the data of total_vaccinations_per_hundred to calculate the total percentage of people who take vaccinated each day. However, the data of total_vaccinations_per_hundred calculate the number of people who take vaccination many times since the covid-19 vaccination need to be taken sencond and third dose by each person. As a result, total percentage of people who take vaccinated each day larger than 100% in this chart.
<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/vaccination_population1.png/></div>

### Improvement On Question4
We choose the data of people_fully_vaccinated_per_hundred to the total percentage of people who take vaccinated each day. The data of people_fully_vaccinated_per_hundred just include the number of people who finish to take all doses of covid-19 vaccination. However, there is still one country which shows that the number people_fully_vaccinated_per_hundred larger than one hundred. In fact, it is impossible in real case, so the imposible data has been deleted. In the end, the new chart shows the right result.
<div align=center><img width = "700" height= "500" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/vaccination_%20population2.png/></div>

## Expanding Content: The situation of vaccination in the United Status
The following three visualizations shows the vaccination situation in United status. The first one is a geometric map which uses color to represent the total vaccination in each state of United Status. 
<div align=center><img width = "800" height= "600" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Total%20Vaccinations%20Given%20in%20the%20United%20States.png/></div>
 
There are two pie charts to represent the percentage of vaccination dose1 by the groups of different ages and races.
<div align=center><img width = "400" height= "400" src =https://github.com/augustinexu/2021Fall_finals/blob/main/plot/age.png/></div>
<div align=center><img width = "400" height= "400" src = https://github.com/augustinexu/2021Fall_finals/blob/main/plot/race.png/></div>

## Hypotheses 
### 1.The urbanization rate was positively correlated to Fully Vaccinated Rate in each state in the United States.
<div align=center><img width = "700" height= "500" src =https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Urbanization%20Rate%20and%20Fully%20vaccinated%20Rate.png/></div>

As we can see in the chart, the blue bars show the urbanization rate, and the state has been arranged according to the rate of urbanization. As the rate of urbanization increasing, the data of Fully Vaccinated Rate has no obviously increasing. Therefore, this Hypothesis is wrong.

### 2.The Income level was positively correlated to Fully Vaccinated Rate in each state in the United States.
<div align=center><img width = "700" height= "500" src =https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Income%20level%20and%20Fully%20vaccinated%20rate%20for%20each%20state(excluded%20NY).png/></div>
The hypoesis is rejected. The chart represents that the state with higher income rate do not necessarily have higher fully vaccinated rate.

### 3.The rate of fully vaccinated was negatively correlated to the new cases of positivity of covid-19.
<div align=center><img width = "1100" height= "350" src =https://github.com/augustinexu/2021Fall_finals/blob/main/plot/Positivity%20Trend%20and%20Fully%20Vaccinated%20Trend1.png/></div>
Between December 2020 to June 2021, the rate of fully vaccinated increased rapidly, and the daily new cases of positivity  decreased as well. However, after June 2021, although the rate of fully vaccinated still increased with a gentle speed, the daily new cases of positivity increased firstly. Therefore, this Hypothesis is rejected. Excepting the rate of fully vaccinated, there are some other elements which impact the new cases of positivity of covid-19.

