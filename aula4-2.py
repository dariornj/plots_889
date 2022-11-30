# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']
types = df['variety'].unique()

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
# ax.plot(1,1,1, marker = 'o')

df1 = df[df['variety'] == types[0]]
df2 = df[df['variety'] == types[1]]
df3 = df[df['variety'] == types[2]]


ax.scatter(df1['sepal_length'], df1['sepal_width'], df1['petal_length'], label = types[0])
ax.scatter(df2['sepal_length'], df2['sepal_width'], df2['petal_length'], label = types[1])
ax.scatter(df3['sepal_length'], df3['sepal_width'], df3['petal_length'], label = types[2])
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
ax.legend()
plt.show()