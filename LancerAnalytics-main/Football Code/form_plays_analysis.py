import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('DLS.csv')

input1 = input("Please input the Down Ex(1,2,3,4): ")
input2 = input("Please input your highest distance, if you do not want a baseline distance please put 100:  ")
input7 = input("Please put baseline distance: ")
input4 = input("ODK: ")
distance = list(df.DN)
filtered = df[(df['ODK'] == input4) & (df['DN'] == int(input1)) & (df['DIST'] <= int(input2)) & (df['DIST'] >= int(input7))]



n = list(filtered.OFFFORM)

x = []
y = []
for i in filtered.OFFFORM:
  y.append(str(i))
  x.append(float(n.count(i)))

plt.xlabel('Number of Times Used')
plt.ylabel('Off form')
plt.barh(y, x, align = 'center', alpha = 0.5, color = 'gold')
scale_factor = 1
plt.xlim(0 * scale_factor, 10 * scale_factor)
plt.savefig('offform.jpg',bbox_inches='tight', dpi=150)


m = list(filtered.PLAYTYPE)
f = []
g = []
for i in filtered.PLAYTYPE:
  f.append(str(i))
  g.append(float(m.count(i)))

plt.xlabel('Number of Times Used')
plt.ylabel('OFFFORM')
plt.barh(f, g, align = 'center', alpha = 0.5, color = 'gold')
scale_factor = 1
plt.xlim(0 * scale_factor, 20 * scale_factor)
plt.savefig('playtype.png',bbox_inches='tight', dpi=150)
plt.plot(figsize=(20,4))



q = df[(df['PLAYTYPE'] == 'Run') & (df['ODK'] == 'O')]
print(sum(list(q.GNLS))/len(list(q.GNLS)))



