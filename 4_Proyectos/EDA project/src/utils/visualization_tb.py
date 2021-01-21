import pandas as pd 
import numpy as np 
import datetime as dt
import os

import matplotlib.pyplot as plt
import seaborn as sns

def label_fig(title=None, xlab=None, ylab=None, tit_size=15):
    if title:
        plt.title(title, fontsize=tit_size)
    if xlab:
        plt.xlabel(xlab)
    if ylab:
        plt.ylabel(ylab)

def column_pie(dataset, column=None, n_to_show=6):

    if column:
        ordered_by_col = dataset.groupby(f'{column}')[f'{column}'].count().sort_values(ascending=False)
    else:
        ordered_by_col = dataset.count().sort_values(ascending=False)

    plt.figure(figsize=(8,8))

    sns.set()

    rest = ordered_by_col.values[n_to_show:].sum()
    count_list = list(ordered_by_col.values[:n_to_show]) + [rest]
    labels = list(ordered_by_col.index[:n_to_show]) + ['otros']


    plt.pie(count_list, labels=labels, autopct='%1.0f%%')

def col_time_series(dataset, column, time_period, agg='mean', colour=8):
    sns.set()
    col= sns.color_palette()
    movies_Y = dataset.groupby(dataset.release_date.dt.to_period(f'{time_period}')).agg(f'{agg}')
    x_ax = movies_Y[column].index.to_timestamp()
    y_ax = movies_Y[column].values

    plt.figure(figsize=(10,6))
    plt.plot(x_ax, y_ax, color=col[colour])

def count_bar(dataset, ascen=True):
    sns.set()
    df_count = dataset.count().sort_values(ascending=ascen)
    plt.figure(figsize=(13,6))
    for i,el in enumerate(df_count):
        x = (el/df_count.sum())*100
        label = df_count.index[i]
        plt.barh(label, x)

def without_0_hist(dataset, column, bin=10, without_0s = True, colour=0):
    sns.set()
    col = sns.color_palette()
    if without_0s:
        df = dataset[dataset[f'{column}'] > 0]
    else:
        df = dataset

    plt.figure(figsize=(8,5))
    plt.hist(df[f'{column}'].values, bins=bin, color=col[colour])

def log_hist(dataset, column, bin=10, without_0s=False, colour=0):
    sns.set()
    col = sns.color_palette()
    if without_0s:
        df = dataset[dataset[f'{column}'] > 0]
    else:
        df = dataset
    
    hist, bins = np.histogram(df[f'{column}'], bins=bin)
    logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
    
    plt.figure(figsize=(8,5))
    plt.hist(df[f'{column}'], bins=logbins, color=col[colour])
    plt.xscale('log')

def dense_plot(serie):
    plt.figure(figsize=(8,5))
    sns.set(palette='husl')
    sns.kdeplot(serie, fill=True)


def save_repo(name):
    root_project = os.path.dirname(os.getcwd())
    plt.savefig(root_project + f'//reports//{name}.jpg')

def two_var_ts(dataset, col1, col2, time_period='Y', agg='mean', colour=(0,2)):
    sns.set()
    col= sns.color_palette()
    df_year = dataset.groupby(dataset.release_date.dt.to_period(time_period)).agg('mean')
    dates = df_year.index.to_timestamp()

    plt.figure(figsize=(10,6))
    #ax = plt.axes()
    plt.plot(dates, df_year[f'{col1}'].values, color=col[colour[0]])
    plt.plot(dates, df_year[f'{col2}'].values, color=col[colour[1]])

def correlation_matrix(dataset):
    plt.figure(figsize=(8,6))
    sns.heatmap(dataset.corr(), cmap="BrBG",annot=True)

def time_spent():
    a = pd.DataFrame({'Búsqueda datos': np.arange(10)})
    b = pd.DataFrame({'Minería de datos':np.arange(40)})
    c = pd.DataFrame({'Visualizaciones': np.arange(35)})
    d = pd.DataFrame({'Estructuración':np.arange(14)})
    e = pd.DataFrame({'Documentación':np.arange(1)})

    tiempo = pd.concat([a,b,c,d,e])
    tiempo = tiempo.count().sort_values(ascending=False)
    plt.figure(figsize=(8,8))

    sns.set()

    count_list = list(tiempo.values)
    labels = list(tiempo.index)
    plt.pie(count_list, labels=labels, autopct='%1.0f%%', explode= (0.02, 0.02,0.02, 0.02,0.02))


