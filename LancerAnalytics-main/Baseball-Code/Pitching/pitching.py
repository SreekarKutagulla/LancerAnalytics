import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

fig, ax = plt.subplots()

custom_lines = [Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='red', lw=4),
                Line2D([0], [0], color='lightblue', lw=4),
                Line2D([0], [0], color='purple', lw=4),
                Line2D([0], [0], color='orange', lw=4),
                Line2D([0], [0], color='magenta', lw=4),Line2D([0], [0], color='yellowgreen', lw=4)]

plt.legend(custom_lines, ['Hit', 'Strike', 'Foul', 'Ball', 'Hit-Ball', 'Foul-Ball', 'Strike-Ball'],loc='upper center', bbox_to_anchor=(1.15, 0.8), shadow=True)



df = pd.read_csv('hit.csv')

h = df[(df['SHFB'] == 'H')]
plt.scatter(h.X,h.Y,s=150,c='green')


s = df[(df['SHFB'] == 'S')]
plt.scatter(s.X,s.Y,s=150,c='red')


f = df[(df['SHFB'] == 'F')]
plt.scatter(f.X,f.Y,s=150,c='lightblue')


b = df[(df['SHFB'] == 'B')]
plt.scatter(b.X,b.Y,s=150,c='purple')


hb = df[(df['SHFB'] == 'HB')]
plt.scatter(hb.X,hb.Y,s=150,c='orange')


fb = df[(df['SHFB'] == 'FB')]
plt.scatter(fb.X,fb.Y,s=150,c='magenta')


sb = df[(df['SHFB'] == 'SB')]
plt.scatter(sb.X,sb.Y,s=150,c='yellowgreen')




#create scatterplot of data with gridlines

#horizantal
plt.plot([-2, -2], [-2, 8], linewidth=2, color='black')
plt.plot([8, 8], [-2, 8], linewidth=2, color='black')
plt.plot([-2, 8], [-2, -2], linewidth=2, color='black')
plt.plot([-2, 8], [0, 0], linewidth=2, color='black')
plt.plot([-2, 8], [2, 2], linewidth=2, color='black')
plt.plot([-2, 8], [4, 4], linewidth=2, color='black')
plt.plot([-2, 8], [6, 6], linewidth=2, color='black')
plt.plot([-2, 8], [8, 8], linewidth=2, color='black')

#vertical
plt.plot([-2, -2], [-2, 8], linewidth=2, color='black')
plt.plot([0, 0], [-2, 8], linewidth=2, color='black')
plt.plot([2, 2], [-2, 8], linewidth=2, color='black')
plt.plot([4, 4], [-2, 8], linewidth=2, color='black')
plt.plot([6, 6], [-2, 8], linewidth=2, color='black')
plt.plot([8, 8], [-2, 8], linewidth=2, color='black')

#inside zone
ax.add_patch(Rectangle((0, 0), 6, 6,
             edgecolor = 'red',
             facecolor = 'none',
             lw=5))



plt.savefig('baseball.jpg',bbox_inches='tight', dpi=150)
