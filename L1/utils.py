from tkinter.messagebox import YES
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from sympy import Q
import numpy as np
from scipy import stats

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
    return data.std()

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

def salintiOutliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df

def plotBar(data, xColumn: str, title=None):
    data.value_counts(sort=False).plot.bar(rot=0)
    plt.xlabel(xColumn)
    plt.ylabel('Kiekis')
    if title is not None:
        plt.title(title)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.autoscale()
    plt.show()

def plotBox(data, column: str, title=None):
    boxplot = data.boxplot(column=[column], grid=False, rot=45, fontsize=15)
    if title is not None:
        plt.title(title)
    plt.show()

def plotScatter(data, xColumn: str, yColumn: str):
    plt.scatter(data[xColumn], data[yColumn], s=60, alpha=0.6, edgecolor='grey', linewidth=1)
    plt.xlabel(xColumn)
    plt.ylabel(yColumn)
    plt.tight_layout()
    plt.show()

def plotScatterMatrix(data):
    axes = pd.plotting.scatter_matrix(data, alpha=0.2)
    for ax in axes.flatten():
        ax.xaxis.label.set_rotation(90)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha('right')
    plt.autoscale()
    plt.show()

def findCorreleation(data):
    correlation_mat = data.corr()
    sns.heatmap(correlation_mat, annot=True)
    plt.show()

def plot(data):
    kategoriniaiAtributai = ['Drive', 'Transmission', 'Turbocharger', 'Supercharger', 'Fuel Type']
    removedOutliers = salintiOutliers(data)
    # for x in removedOutliers:
    #     plotBar(removedOutliers[x], xColumn=x, title=x)

    # tolydiniaiAtributai = ['Year', 'Engine Cylinders', 'Engine Displacement', 'City MPG', 'Highway MPG', 'Annual Fuel Cost', 'Tailpipe CO2 in Grams/Mile']
    # plotScatter(data, xColumn='Tailpipe CO2 in Grams/Mile', yColumn='Year')
    # plotScatter(data, xColumn='Engine Displacement', yColumn='Engine Cylinders')
    # plotScatter(data, xColumn='City MPG', yColumn='Engine Displacement')
    # plotScatter(data, xColumn='Highway MPG', yColumn='Engine Displacement')
    # plotScatter(data, xColumn='Annual Fuel Cost', yColumn='Year')
    # plotScatterMatrix(data)
    plotBox(data[data['Drive'] == 'Rear-Wheel Drive'], column='City MPG', title='City MPG & Rear-Wheel Drive')
    plotBox(data[data['Fuel Type'] == 'Premium'], column='City MPG', title='City MPG & Premium fuel')
    plotBox(data[data['Transmission'] == 'Manual 5-Speed'], column='Engine Cylinders', title='City MPG & Premium fuel')

def normalize(data):
    result = data.copy()
    for x in data:
        max = data[x].max()
        min = data[x].min()
        result[x] = (data[x] - min) / (max - min)
    return result 







