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

