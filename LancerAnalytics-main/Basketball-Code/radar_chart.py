import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
sample_data = pd.read_csv('stats.csv')

df = pd.read_csv('stats.csv')

categories=list(df)[1:]
N = len(categories)
 

values=df.loc[0].drop('Starters').values.flatten().tolist()
values += values[:1]
values
 

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 

ax = plt.subplot(111, polar=True)

plt.xticks(angles[:-1], categories, color='grey', size=8)
 

ax.set_rlabel_position(0)
plt.yticks([1,5,10], ['1','5','10'], color="grey", size=10)
plt.ylim(0,10)
 

ax.plot(angles, values, linewidth=1, linestyle='solid')
 

ax.fill(angles, values, 'b', alpha=0.1)



plt.savefig('radar.jpg',bbox_inches='tight', dpi=150)
