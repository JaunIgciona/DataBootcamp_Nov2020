import pandas as pd
import numpy as np
import json
import re
import utils.folders_tb as fold

def fast_datetime_check(date_column):
    '''
    Checks if column can't be converted to datetime
    '''
    try:
        pd.to_datetime(date_column)
    except ValueError:
        print('Given date string not likely a datetime')

def not_a_datetime_detector(date_column):
    '''
    Returns list of elements in column that can't be converted to datetime
    '''
    l = []
    for i, it in enumerate(date_column):
        try:
            pd.to_datetime(it)
        except:
            l.append(i)
    print(l)
    return l


def series_json_to_list(serie, use_key):
    '''
    Args:
        serie (pd.Series)
        use_key (str): key name to select from series' dicts

    From serie (pd.Series of dicts) returns the useful information from the dict (use_key) in list form 
    '''
    serie = fold.json_prep(serie)

    uniq_vals = set({})

    for i, element in enumerate(serie):
        val_list = []
        for dictio in element:
            val_list.append(dictio[use_key])
            uniq_vals.add(dictio[use_key])
        if i == 0:
            serie_dictio = {i: [val_list]}
        else:
            serie_dictio[i] = [val_list]

    print(f'Número de elemenos únicos ---> {len(uniq_vals)}\n', 'Todos los elementos únicos de la columna:\n',         uniq_vals)
    
    serie_df = pd.DataFrame.from_dict(serie_dictio, orient='index', columns=[serie.name])
    
    return serie_df

def expand_df(serie):
    '''
    Returns new dataframe with elements of serie as columns
    '''
    # Creates column of dictionaries where key = values, from elements of lists in serie
    serie_df = pd.DataFrame.from_dict(serie.apply(lambda x: {gen : gen for gen in x}))
    # Creates dataframe with columns equal to unique values of serie
    serie_expanded = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in serie_df[serie_df.columns[0]].items() ])).transpose()
    
    return serie_expanded
