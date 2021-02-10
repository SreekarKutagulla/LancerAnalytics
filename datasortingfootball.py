import pandas as pd

df = pd.read_csv('test.csv')

input1 = input("Please input the Down Ex(1,2,3,4): ")
input2 = input("Please input your baseline distance, if you do not want a baseline distance please put 100:  ")

input3 = input("Please input a playtype: ")

input4 = input("ODK: ")

distance = list(df.DN)

filtered = df[(df['ODK'] == input4) & (df['DN'] == int(input1)) & (df['DIST'] <= int(input2))& (df['PLAYTYPE'] == input3)]

print(list(filtered.OFFFORM))
print(list(filtered.OFFPLAY))