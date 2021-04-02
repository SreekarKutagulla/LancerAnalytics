import pandas as pd
from matplotlib import pyplot as plt





print('Choose a player from this list: ')


sample_data = pd.read_csv('stats.csv')
print(list(sample_data.Starters))

playerName = input("Enter the Player's First and Last Name: ")
names = list(sample_data.Starters)



def calculateTrueShooting(PTS, FGA, FTA):
  return ((PTS) / (2* (FGA + 0.44 * FTA))) * 100



if playerName in names:
  print('Here is the True Shooting Percentage for ' + playerName + '.')
  playerIndex = names.index(playerName)
  playerProfile = sample_data.loc[playerIndex, :]
  count = calculateTrueShooting(playerProfile.PTS, playerProfile.FGA, playerProfile.FTA) + playerProfile.PTS
  print(calculateTrueShooting(playerProfile.PTS, playerProfile.FGA, playerProfile.FTA))
else:
  print(False)

print(count)
def rate(count1):
  rating = 0
  if count1 <= 45:
    rating = 1
  if 45 < count1 <= 55:
    rating = 2
  if 55 < count1 <= 65:
    rating = 3
  if 65< count1 <= 75:
    rating = 4
  if 75 < count1 <= 85:
    rating = 5
  if 85 < count1 <= 95:
    rating = 6
  if 95 < count1 <= 105:
    rating = 7
  if 105 < count1 <= 115:
    rating = 8
  if 115 < count1 < 125:
    rating = 9
  if count > 125:
    rating = 10

  return rating

print(rate(count))



#Calculates the PER for the whole team


#print(sample_data)
counter = 0
print('Miami Heat at Philadelphia 76ers, January 12, 2021 True Shooting: ')
for i in sample_data.Starters:
  playerIndex = names.index(i)
  playerProfile = sample_data.loc[playerIndex, :]
  print(i + ': ' + str(calculateTrueShooting(playerProfile.PTS, playerProfile.FGA, playerProfile.FTA)))

for i in sample_data.Starters:
  playerIndex = names.index(i)
  playerProfile = sample_data.loc[playerIndex, :]
  print(i + ':' + str(rate(calculateTrueShooting(playerProfile.PTS, playerProfile.FGA, playerProfile.FTA) + playerProfile.PTS)))





x = []
y = []
names = list(sample_data.Starters)
for i in sample_data.Starters:
  y.append(str(i))
  playerIndex = names.index(i)
  playerProfile = sample_data.loc[playerIndex, :]
  x.append(float(calculateTrueShooting(playerProfile.PTS, playerProfile.FGA, playerProfile.FTA)))
plt.xlabel('True Shooting Percentage')
plt.ylabel('Miami Heat Players')
plt.title('Miami Heat at Philadelphia 76ers, January 12, 2021')
plt.barh(y, x, align = 'center', alpha = 0.5, color = 'pink')
scale_factor = 2
plt.xlim(0 * scale_factor, 50 * scale_factor)
plt.show()
