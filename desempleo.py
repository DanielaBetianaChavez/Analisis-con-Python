"""import pandas
filename = 'datosE.csv'
data = pandas.read_csv(filename, header=0)

print(data.shape)
print (data.head(5))"""

"""Muestre un marco de datos en el que el desempleo sea superior al 8,5%. """

import pandas as pd
from zmq import RATE
data = pd.read_csv('datosE.csv', header=0)
print (data)
print(data['RATE'])
df1= data[data['RATE']>=8.5]
print(df1)


