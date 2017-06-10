import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import statistics as stats
import plotly.plotly as py
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

data_file = "data.csv"
data = pd.read_csv(data_file)

df = pd.DataFrame(data)
def findAvg(topic):
    l = []
    for d in df.iterrows():
        if d[1]['Topic'] == topic:
            l.append(d)
    return l

avgObese = findAvg('Obesity / Weight Status')
avgDiet = findAvg('Fruits and Vegetables - Behavior')
avgActivity = findAvg('Physical Activity - Behavior')

avgObeseList = [x[1] for x in avgObese]
obese_df = pd.DataFrame(avgObeseList)

avgDietList = [x[1] for x in avgDiet]
diet_df = pd.DataFrame(avgDietList)

avgActivityList = [x[1] for x in avgActivity]
activity_df = pd.DataFrame(avgActivityList)

groupedDiet = diet_df.groupby(['LocationDesc'])['Data_Value'].mean()
groupedActivity = activity_df.groupby(['LocationDesc'])['Data_Value'].mean()
groupedObese = obese_df.groupby(['LocationDesc'])['Data_Value'].mean()

obesePd = pd.DataFrame(groupedObese).reset_index()
obesePd = obesePd.drop(obesePd.index[[11,28,41]])
obesePd = obesePd.reset_index()

dietPd = pd.DataFrame(groupedDiet).reset_index()
dietPd = dietPd.drop(dietPd.index[[11,28,41]])
dietPd = dietPd.reset_index()

actPd = pd.DataFrame(groupedActivity).reset_index()
actPd = actPd.drop(actPd.index[[11,28,41]])
actPd = actPd.reset_index()

tmpdf = groupedObese.to_frame().reset_index()
tmpdf = tmpdf.drop(tmpdf.index[[11,28,41]])
tmpdf.columns = ['State', 'Percentage Obese']

# Manually extracted from wiki LOL
lifeExpect = [ 75.4, 78.3, 79.6, 76, 80.8, 80, 80.8, 78.4, 76.5, 79.4, 77.2, 81.3, 79.5, 79.0, 77.6, 79.7, 78.7, 76.0, 
75.7, 79.2, 78.8, 80.5, 78.2, 81.1, 75.0, 77.5, 78.5, 79.8, 78.1, 80.3, 80.3, 78.4, 80.5, 77.8, 79.5, 77.8, 75.9, 79.5, 
78.5, 79.9, 77, 79.5, 76.3, 78.5, 80.2, 80.5, 79, 79.9, 75.4, 80, 78.3 ]


dietList = dietPd.Data_Value.tolist()
activityList = actPd.Data_Value.tolist()
obeseList = obesePd.Data_Value.tolist()

stateList = tmpdf['State'].tolist()
zipped = zip(stateList, obeseList, dietList, activityList, lifeExpect)

# groupDf = groupedData.to_frame().reset_index()
groupDf = pd.DataFrame(zipped)
groupDf.columns = ['state', 'obese', 'diet', 'activity', 'life expectancy']
groupDf = groupDf.sort_values('life expectancy')

groupDf.plot(y=["life expectancy", "obese","diet", "activity"], x="state", figsize = (20,10))
plt.show()
