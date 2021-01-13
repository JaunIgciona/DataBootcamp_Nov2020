import pandas as pd 
import numpy as np 
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns

def label_fun(title=None, xlab=None, ylab=None):
    if title:
        plt.title(title, fontsize=20)
    if xlab:
        plt.xlabel(xlab)
    if ylab:
        plt.ylabel(ylab)

def column_pie(dataset, *column, n_to_show):

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

def col_time_series(dataset, column, time_period, agg='mean'):
    sns.set()
    movies_Y = dataset.groupby(dataset.release_date.dt.to_period(f'{time_period}')).agg(f'{agg}')
    x_ax = movies_Y[column].index.to_timestamp()
    y_ax = movies_Y[column].values

    plt.figure(figsize=(10,6))
    plt.plot(x_ax, y_ax)

def count_bar(dataset, ascen=True):
    sns.set()
    df_count = dataset.count().sort_values(ascending=ascen)
    plt.figure(figsize=(13,6))
    for i,el in enumerate(df_count):
        x = (el/df_count.sum())*100
        label = df_count.index[i]
        plt.barh(label, x)

def without_0_hist(dataset, column, bin):
    sns.set()
    df_without_0 = dataset[dataset[f'{column}'] > 0]

    plt.figure(figsize=(10,6))
    plt.hist(df_without_0[f'{column}'].values, bins=bin)

def log_hist(dataset, column, bin, without_0s=False):
    sns.set()
    if without_0s:
        df = dataset[dataset[f'{column}'] > 0]
    else:
        df = dataset
    
    hist, bins = np.histogram(df[f'{column}'], bins=18)
    logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
    
    plt.figure(figsize=(10,6))
    plt.hist(df[f'{column}'], bins=logbins)
    plt.xscale('log')

