import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def readData(fileName):
    mydataset = pd.read_csv(fileName)
    return mydataset

def rastiAtributuSkaiciu(data):
    return data.count()

def rastiTrukstamuAtributuProcenta(data):
    nullValues = data.isnull().sum() * 100 / len(data)
    return nullValues

def rastiAtributuKardinalumus(data):
    return data.nunique()

def rastiMin(data):
    return data.min()

def rastiMax(data):
    return data.max()

def rastiKvartilius(data):
    return data.quantile([0.25,0.75])

def rastiVidurkius(data):
    return data.mean()

def rastiMedianas(data):
    return data.median()

def rastiStandartiniusNuokrypius(data):
    return data.median()

def rastiModas(data):
    # return data.mode()
    return pd.DataFrame({'Columns': data.columns,
                         'Val': [Counter(data[x]).most_common()[0]  for x in data]})

def rastiModosDaznumus(data):
    return pd.DataFrame({'Columns': data.columns,
                         'Val': [data[x].isin(data[x].mode()).sum() for x in data]})

def rastiModuDaznumuProcentus(data):
    return pd.DataFrame({'Columns': data.columns,
                         'Val': [data[x].isin(data[x].mode()).sum()*100/len(data[x])  for x in data]})

def rastiAntrosModosDaznumus(data):
    return pd.DataFrame({'Columns': data.columns,
                         'Val': [Counter(data[x]).most_common()[1]  for x in data]})

def rastiAntruModuDaznumuProcentus(data):
    return pd.DataFrame({'Columns': data.columns,
                         'Val': [data[x].isin([Counter(data[x]).most_common()[1][0]]).sum()*100/len(data[x])  for x in data]})                        
