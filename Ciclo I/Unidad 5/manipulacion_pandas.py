from os import name
import numpy as np
import pandas as pd
from pandas.io import json
import requests
import math

from requests.api import head

respuesta = requests.get('http://citibikenyc.com/stations/json')
data = json.loads(respuesta.content)
dataDF = pd.DataFrame(data['stationBeanList'])
dataDF = dataDF.loc[:,['id', 'stationName', 'availableDocks', 'totalDocks', 'latitude']]

dataDF.set_index(['id'])
# dataDF.index = dataDF['id']
# dataDF.drop(['id'], axis=1, inplace=True)
dataDF.drop([72], inplace=True)

# print(dataDF['stationName'][79])
# print(dataDF.stationName[79])

# print(list(dataDF.iloc[79,:]))
# print(dataDF.shape)
dataDF = dataDF.append(list(dataDF.iloc[79,:]), ignore_index=True)
dataDF = dataDF.append(dataDF.iloc[79,:], ignore_index=True)
dataDF = dataDF.append(dataDF.iloc[512,:], ignore_index=False)

# print(dataDF.tail(10),'\n')

# print(dataDF.notna().tail(10))
# print(dataDF[dataDF['latitude'].notna()].tail(10))
# print(dataDF.drop_duplicates([0], keep='last', inplace=True))

unicos_availableDocks = set(dataDF['availableDocks'].unique())
unicos_totalDocks = set(dataDF['totalDocks'].unique())

unicos = list(unicos_availableDocks.union(unicos_totalDocks))

print(dataDF.dropna(how='all', inplace=True))

# dataDF['availableDocks'] = dataDF['availableDocks'].apply(lambda x: math.pow(x,3))
dataDF['availableDocks'] = dataDF['availableDocks'].apply(math.sqrt)

totalizar = dataDF['totalDocks'].sum()
# print(totalizar)

dataDF = pd.read_json('http://citibikenyc.com/stations/json')
# print(dataDF['stationBeanList'].head(5))
# print(dict(dataDF['stationBeanList']))
dataDF = pd.DataFrame(dict(dataDF['stationBeanList']))
print(dataDF.head(5))
# print(dataDF.transpose().head(5))

dataDF.loc['totalDocks',:] = dataDF.loc['totalDocks',:].apply(math.sqrt)
totalizar = dataDF.loc['totalDocks',:].sum()
