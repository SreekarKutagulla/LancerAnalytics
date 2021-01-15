# Total Rebound Percentage (available since the 1970-71 season in the NBA); the formula is 100 * (TRB * (Tm MP / 5)) / (MP * (Tm TRB + Opp TRB)). Total rebound percentage is an estimate of the percentage of available rebounds a player grabbed while he was on the floor.

import pandas as pd
from matplotlib import pyplot as plt

my_team = pd.read_csv('HEAT.csv')
opponent_team = pd.read_csv('SIXERS.csv')


OTTR = sum(opponent_team.TRB)
TTR = sum(my_team.TRB)
TMP = sum(my_team.MP)


print('Choose a player from this list: ')
print(list(my_team.Starters))
playerName = input("Enter the Player's First and Last Name: ")
names = list(my_team.Starters)

def calculateRebPercentage(PlayerReb, PlayerMin):
  return (100 * PlayerReb * PlayerMin) / (PlayerMin * (TTR + OTTR))
counter = 0 
if playerName in names:
  print('Here is the rebounding percentage for ' + playerName + '.')
  playerIndex = names.index(playerName)
  playerProfile = my_team.loc[playerIndex, :]
  count = calculateRebPercentage(playerProfile.TRB, playerProfile.MP)
else:
  print('This is not a valid player.')
print(count)


counter = 0
print('Miami Heat at Philadelphia 76ers, January 12, 2021 True Shooting: ')
for i in my_team.Starters:
  playerIndex = names.index(i)
  playerProfile = my_team.loc[playerIndex, :]
  print(i + ': ' + str(int(calculateRebPercentage(playerProfile.TRB, playerProfile.MP))))



x = []
y = []
names = list(my_team.Starters)
for i in my_team.Starters:
  y.append(str(i))
  playerIndex = names.index(i)
  playerProfile = my_team.loc[playerIndex, :]
  x.append(str(int(calculateRebPercentage(playerProfile.TRB, playerProfile.MP))))
plt.xlabel('Rebounding Percentage')
plt.ylabel('Miami Heat Players')
plt.title('Miami Heat at Philadelphia 76ers, January 12, 2021')
plt.barh(y, x, align = 'center', alpha = 0.5, color = 'pink')
scale_factor = 0.2
plt.xlim(0 * scale_factor, 50 * scale_factor)
plt.savefig('bar.jpg',bbox_inches='tight', dpi=150)
