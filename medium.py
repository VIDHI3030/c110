
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random
import pandas as pd 
import csv 
df=pd.read_csv("csv/medium_data.csv")
data= df["reading_time"].tolist()
#fig=ff.create_distplot([data],["average"],show_hist=False)
#fig.show()
def randomsetofmeans(c):
    dataSet=[]
    for i in range(0,c):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean 

def showFig(meanList):
    mean=statistics.mean(meanList)
    fig=ff.create_distplot([meanList],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,12],mode="lines",name="mean"))
    fig.show()

def setUp():
    meanList=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanList.append(setofmeans)
    showFig(meanList)
    samplingMean=statistics.mean(meanList)
    print("samplingmean ",samplingMean)
    samplingStd=statistics.stdev(meanList)
    print("sampling standard devition ",samplingStd)

populationmean=statistics.mean(data)
print(populationmean)
populationstd=statistics.stdev(data)
print("standard deviation ",populationstd)
setUp()

