import pandas as pd
from matplotlib import pyplot as plt

# http://www.rustylarue.com/more-than-94rsquo/player-efficiency-stats#:~:text=Simple%20PER%20is%20calculated%20as,%2B%20Blocks%20%2B%20Steals%20%2D%20Turnovers.

#formula for simple PER

#Choose the player to calculate the PER for

print('Choose a player from this list: ')


sample_data = pd.read_csv('stats2.csv')
print(list(sample_data.Starters))
# (2FG Made*2) - (2FG Attempted*.75) + (3FG Made*3) – (3FG Attempted*.84) + (FT Made) - (FT Attempted*-.65) + Rebounds + Assists + Blocks + Steals - Turnovers
playerName = input("Enter the Player's First and Last Name: ")
names = list(sample_data.Starters)


#efficiency calculator
def calculatePER (POINTS, TWOfgATT, THREEfgATT, FTMADE, FTATT, REB, ASS, BLOCK, STEAL, TOV):
  return POINTS - (TWOfgATT*.75) - (THREEfgATT * .84) + (FTMADE) - (FTATT *-.65) + REB + ASS + BLOCK + STEAL - (TOV * 1.289)



if playerName in names:
  print('Here is the efficency score for ' + playerName + '.')
  playerIndex = names.index(playerName)
  playerProfile = sample_data.loc[playerIndex, :]
  print(calculatePER(playerProfile.PTS, playerProfile.FGA - playerProfile.THREEPA, playerProfile.THREEP, playerProfile.FT, playerProfile.FTA, playerProfile.TRB, playerProfile.AST, playerProfile.BLK, playerProfile.STL, playerProfile.TOV))
else:
  print(False)




#Caclulates the PER for thr whole team


#print(sample_data)
counter = 0
print('Miami Heat at Philadelphia 76ers, January 12, 2021 PER: ')
for i in sample_data.Starters:
  playerIndex = names.index(i)
  playerProfile = sample_data.loc[playerIndex, :]
  print(i + ': ' + str(calculatePER(playerProfile.PTS, playerProfile.FGA - playerProfile.THREEPA, playerProfile.THREEP, playerProfile.FT, playerProfile.FTA, playerProfile.TRB, playerProfile.AST, playerProfile.BLK, playerProfile.STL, playerProfile.TOV)))





'''
Graphs the PER as a horizontal bar chart for the whole team

'''




x = []
y = []
names = list(sample_data.Starters)
for i in sample_data.Starters:
  y.append(str(i))
  playerIndex = names.index(i)
  playerProfile = sample_data.loc[playerIndex, :]
  x.append(float(calculatePER(playerProfile.PTS, playerProfile.FGA - playerProfile.THREEPA, playerProfile.THREEP, playerProfile.FT, playerProfile.FTA, playerProfile.TRB, playerProfile.AST, playerProfile.BLK, playerProfile.STL, playerProfile.TOV)))
plt.xlabel('PER Rating')
plt.ylabel('Miami Heat Players')
plt.title('Miami Heat at Philadelphia 76ers, January 12, 2021')
plt.barh(y, x, align = 'center', alpha = 0.5, color = 'pink')
scale_factor = 1
plt.xlim(0 * scale_factor, 50 * scale_factor)
plt.show()
