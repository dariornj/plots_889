# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']

# Montando plots em uma diferente

fig = plt.figure()
spec = fig.add_gridspec(3, 3)

ax0 = fig.add_subplot(spec[0,:])
ax0.plot(df['sepal_length'])

ax1 = fig.add_subplot(spec[1,0])
ax1.scatter(df['petal_length'], df['petal_width'])

ax2 = fig.add_subplot(spec[1,1])
ax2.plot(df['sepal_width'], color = 'r')

ax3 = fig.add_subplot(spec[1:, 2])
ax3.plot(df['sepal_width'], color = 'r')

ax4 = fig.add_subplot(spec[2, :2])
ax4.plot(df['variety'])


plt.show()
