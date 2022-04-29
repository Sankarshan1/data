import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv('medium_data.csv')

data=df['responses'].tolist()

def random_set_off_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],['responses'],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        setofmean=random_set_off_mean(100)
        mean_list.append(setofmean)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print('samplemean',mean)
setup()   