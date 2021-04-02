import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle


# Create DataFrame
shot_df = pd.read_csv('shotchartdata.csv')
shot_df['Made'] = shot_df['Made'].astype('float')
shot_df['Attempts'] = shot_df['Attempts'].astype('float')

# Calculate Efficiency
left_corner_eff = shot_df.iloc[0]
q = (left_corner_eff['Made'] / left_corner_eff['Attempts']) * 100

left_wing_eff = shot_df.iloc[1]
w = (left_wing_eff['Made'] / left_wing_eff['Attempts']) * 100

left_short_eff = shot_df.iloc[2]
e = (left_short_eff['Made'] / left_short_eff['Attempts']) * 100

center_inside_eff = shot_df.iloc[3]
r = (center_inside_eff['Made'] / center_inside_eff['Attempts']) * 100

center_point_eff = shot_df.iloc[4]
t = (center_point_eff['Made'] / center_point_eff['Attempts']) * 100

paint_eff = shot_df.iloc[5]
u = (paint_eff['Made'] / paint_eff['Attempts']) * 100

right_corner_eff = shot_df.iloc[6]
i = (right_corner_eff['Made'] / right_corner_eff['Attempts']) * 100

right_wing_eff = shot_df.iloc[7]
o = (right_wing_eff['Made'] / right_wing_eff['Attempts']) * 100

right_short_eff = shot_df.iloc[8]
p = (right_short_eff['Made'] / right_short_eff['Attempts']) * 100

# Rectangle Colors
red = 'r'
green = 'g'
yellow = 'y'

# Make Variables for Made/Attempted Ratios
lc = str(left_corner_eff['Made']) + "/" + str(left_corner_eff['Attempts'])
lw = str(left_wing_eff['Made']) + "/" + str(left_wing_eff['Attempts'])
ls = str(left_short_eff['Made']) + "/" + str(left_short_eff['Attempts'])
ci = str(center_inside_eff['Made']) + "/" + str(center_inside_eff['Attempts'])
cp = str(center_point_eff['Made']) + "/" + str(center_point_eff['Attempts'])
pe = str(paint_eff['Made']) + "/" + str(paint_eff['Attempts'])
rc = str(right_corner_eff['Made']) + "/" + str(right_corner_eff['Attempts'])
rw = str(right_wing_eff['Made']) + "/" + str(right_wing_eff['Attempts'])
rs = str(right_short_eff['Made']) + "/" + str(right_short_eff['Attempts'])

# Function to draw basketball court
def create_court(ax, color):
  # Short corner 3PT lines
  ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
  ax.plot([220, 220], [0, 140], linewidth=2, color=color)
  # 3PT Arc
  ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
  # Lane and Key
  ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
  ax.plot([80, 80], [0, 190], linewidth=2, color=color)
  ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
  ax.plot([60, 60], [0, 190], linewidth=2, color=color)
  ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
  ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))
  # Rim
  ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))   
  # Backboard
  ax.plot([-30, 30], [40, 40], linewidth=2, color=color)
  # Remove ticks
  ax.set_xticks([])
  ax.set_yticks([])
  # Set axis limits
  ax.set_xlim(-250, 250)
  ax.set_ylim(0, 470)
  # General plot parameters
  mpl.rcParams['font.family'] = 'Avenir'
  mpl.rcParams['font.size'] = 18
  mpl.rcParams['axes.linewidth'] = 2
  
  # Create Zones - Top, Left, Right Wing
  ax.plot([-90, -110], [287,500], linewidth=3, color=color)
  ax.plot([90,110], [287, 500], linewidth=3, color=color)
  # Create Zones - Left, Right Corner
  ax.plot([-252,-221], [150, 150], linewidth=3, color=color)
  ax.plot([252,221], [150, 150], linewidth=3, color=color)
  # Create Zones - Top Key, Left, Right Short Corner
  ax.plot([-84,-195], [180, 210], linewidth=3, color=color)
  ax.plot([85,195], [180, 210], linewidth=3, color=color)

  # Left Corner
  if q >= 40:
    ax.add_patch(Rectangle((-250, 0), 27, 150,linewidth=1, edgecolor=green, facecolor=green))
  elif q < 40 and q >= 25:
    ax.add_patch(Rectangle((-250, 0), 27, 150,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif q < 25 and q >= 0:
    ax.add_patch(Rectangle((-250, 0), 27, 150,linewidth=1, edgecolor=red, facecolor=red))
    
  # Left Wing
  if w >= 40:
    ax.add_patch(Rectangle((-220, 290), 100, 100,linewidth=1, edgecolor=green, facecolor=green, angle=5.5))
  elif w < 40 and w >= 25:
    ax.add_patch(Rectangle((-220, 290), 100, 100,linewidth=1, edgecolor=yellow, facecolor=yellow, angle=5.5))
  elif w < 25 and w >= 0:
    ax.add_patch(Rectangle((-220, 290), 100, 100,linewidth=1, edgecolor=red, facecolor=red, angle=5.5))

  # Left Short
  if e >= 50:
    ax.add_patch(Rectangle((-200, 35), 100, 100,linewidth=1, edgecolor=green, facecolor=green))
  elif e < 50 and e >= 30:
    ax.add_patch(Rectangle((-200, 35), 100, 100,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif e < 30 and e >= 0:
    ax.add_patch(Rectangle((-200, 35), 100, 100,linewidth=1, edgecolor=red, facecolor=red))

  # Center Inside 
  if r >= 50:
    ax.add_patch(Rectangle((-65, 199), 127, 83,linewidth=1, edgecolor=green, facecolor=green))
  elif r < 50 and r >= 30:
    ax.add_patch(Rectangle((-65, 199), 127, 83,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif r < 20 and r >= 0:
    ax.add_patch(Rectangle((-65, 199), 127, 83,linewidth=1, edgecolor=red, facecolor=red))

  # Center Point
  if t >= 40:
    ax.add_patch(Rectangle((-50, 335), 100, 100,linewidth=1, edgecolor=green, facecolor=green))
  elif t < 40 and t >= 25:
    ax.add_patch(Rectangle((-50, 335), 100, 100,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif t < 25 and t >= 0:
    ax.add_patch(Rectangle((-50, 335), 100, 100,linewidth=1, edgecolor=red, facecolor=red))
  
  #Center Paint 
  if t >= 70:
    ax.add_patch(Rectangle((-80, 0), 160, 190,linewidth=1, edgecolor=green, facecolor=green))
  elif t < 70 and t >= 55:
    ax.add_patch(Rectangle((-80, 0), 160, 190,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif t < 50 and t >= 0:
    ax.add_patch(Rectangle((-80, 0), 160, 190,linewidth=1, edgecolor=red, facecolor=red))
    
  # Right Corner
  if i >= 40:
    ax.add_patch(Rectangle((220, 0), 27, 150,linewidth=1, edgecolor=green, facecolor=green))
  elif i < 40 and i >= 25:
    ax.add_patch(Rectangle((220, 0), 27, 150,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif o < 25 and i >= 0:
    ax.add_patch(Rectangle((220, 0), 27, 150,linewidth=1, edgecolor=red, facecolor=red))

  # Right Wing
  if o >= 40:
    ax.add_patch(Rectangle((120, 295), 100, 100,linewidth=1, edgecolor=green, facecolor=green, angle=-5.5))
  elif o < 40 and o >= 25:
    ax.add_patch(Rectangle((120, 295), 100, 100,linewidth=1, edgecolor=yellow, facecolor=yellow, angle=-5.5))
  elif o < 25 and o >= 0:
    ax.add_patch(Rectangle((120, 295), 100, 100,linewidth=1, edgecolor=red, facecolor=red, angle=-5.5))

  # Right Short
  if p >= 50:
    ax.add_patch(Rectangle((100, 35), 100, 100,linewidth=1, edgecolor=green, facecolor=green))
  elif p < 50 and p >= 30:
    ax.add_patch(Rectangle((100, 35), 100, 100,linewidth=1, edgecolor=yellow, facecolor=yellow))
  elif p < 30 and p >= 0:
    ax.add_patch(Rectangle((100, 35), 100, 100,linewidth=1, edgecolor=red, facecolor=red))

  # Put Text On Chart
  font = {'family': 'DejaVu Sans',
        'color':  'black',
        'weight': 'bold',
        'size': 10
        }
  # Center 
  plt.text(-30, 410, str(round(t,1)) + "%", fontdict=font)
  plt.text(-33, 388, cp, fontdict=font)
  plt.text(-30, 260, str(round(r,1)) + "%", fontdict=font)
  plt.text(-38, 215, ci, fontdict=font)
  plt.text(-30, 156, str(round(u,1)) + "%", fontdict=font)
  plt.text(-32, 99, pe, fontdict=font)
  # Right Zones
  plt.text(147, 362, str(round(o,1)) + "%", fontdict=font,rotation=-5.5)
  plt.text(141, 341, rw, fontdict=font, rotation=-5.5)
  plt.text(123, 110, str(round(p,1)) + "%", fontdict=font)
  plt.text(117, 88, rs, fontdict=font)
  plt.text(225, 85, str(round(i,1)) + "%", fontdict=font, rotation=-90)
  plt.text(225, 10, rc, fontdict=font, rotation=-90)
  # Left Zones
  plt.text(-208, 368, str(round(w,1)) + "%", fontdict=font,rotation=5.5)
  plt.text(-211, 346, lw, fontdict=font, rotation=5.5)
  plt.text(-178, 110, str(round(e,1)) + "%", fontdict=font)
  plt.text(-185, 88, ls, fontdict=font)
  plt.text(-244, 10, str(round(q,1)) + "%", fontdict=font, rotation=90)
  plt.text(-244, 71, lc, fontdict=font, rotation=90)
  
# Draw basketball court
fig = plt.figure(figsize=(4, 3.76))
ax = fig.add_axes([0, 0, 1, 1])
ax = create_court(ax, 'black')

plt.title('Shot Chart')

plt.savefig('shotchart.jpg',bbox_inches='tight', dpi=150)
plt.show()