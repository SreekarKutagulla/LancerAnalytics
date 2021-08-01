import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D


df = pd.read_csv('hitting.csv')

total_hits = df['Hits'].sum() + df['Outs'].sum()
print(total_hits)

left = df.iloc[0]
left_eff = str(round(((left['Hits']/(left['Hits'].sum()+left['Outs'].sum())) * 100),2)) + "%"

center = df.iloc[1]
center_eff = str(round(((center['Hits']/(center['Hits'].sum()+center['Outs'].sum())) * 100), 2)) + "%"

right = df.iloc[2]
right_eff = str(round(((right['Hits']/(right['Hits'].sum()+right['Outs'].sum())) * 100), 2)) + "%"

print(left_eff)
print(center_eff)
print(right_eff)



plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
im = plt.imread("b.png")
fig, ax = plt.subplots()
im = ax.imshow(im, extent=[0, 1000, 0, 700])


plt.plot([300, 500], [700, 95], linewidth=0.5, color='black')

plt.plot([500, 700], [95, 700], linewidth=0.5, color='black')


x = [300,500,500,700]
y = [700,95,95,700]

x2 =[0,0,300,500]
y2=[500,700,700,85]

x3=[1000,1000,700,500]
y3=[500,700,700,85]

if (center['Hits'].sum()+center['Outs'].sum())/total_hits>=0.3:
  plt.fill(x,y,color='lightgreen', alpha=0.2)

if 0.3>(center['Hits'].sum()+center['Outs'].sum())/total_hits>=0.2:
  plt.fill(x,y,color='yellow', alpha=0.2)

if 0.2>(center['Hits'].sum()+center['Outs'].sum())/total_hits>=0.05:
  plt.fill(x,y,color='red', alpha=0.2)


if (left['Hits'].sum()+left['Outs'].sum())/total_hits>=0.3:
  plt.fill(x2,y2,color='lightgreen', alpha=0.2)

if 0.3>(left['Hits'].sum()+left['Outs'].sum())/total_hits>=0.2:
  plt.fill(x2,y2,color='yellow', alpha=0.2)

if 0.2>(left['Hits'].sum()+left['Outs'].sum())/total_hits>=0.05:
  plt.fill(x2,y2,color='red', alpha=0.2)


if (right['Hits'].sum()+right['Outs'].sum())/total_hits>=0.3:
  plt.fill(x3,y3,color='lightgreen', alpha=0.2)

if 0.3>(right['Hits'].sum()+right['Outs'].sum())/total_hits>=0.2:
  plt.fill(x3,y3,color='yellow', alpha=0.2)

if 0.2>(right['Hits'].sum()+right['Outs'].sum())/total_hits>=0.05:
  plt.fill(x3,y3,color='red', alpha=0.2)



plt.savefig('baseball_hitter.jpg',bbox_inches='tight', dpi=300)
