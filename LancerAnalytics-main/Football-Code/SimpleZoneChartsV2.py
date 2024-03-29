import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import glob
import sys
import pandas as pd

for filename in glob.glob('*'):
  if '.csv' in filename:
    os.rename(filename, 'data.csv')

for filename in glob.glob('*'):
  if '.txt' in filename:
    os.remove(filename)

sys.stdout = open('charts.txt', 'w')

data_df = pd.read_csv('data.csv')
data_df = data_df.rename(columns={'PLAY #': 'PLAY_#', 'YARD LN': 'YARD_LN', 'PLAY TYPE': 'PLAY_TYPE', 'OFF FORM': 'OFF_FORM', 'OFF PLAY': 'OFF_PLAY','OFF STR': 'OFF_STR', 'PLAY DIR': 'PLAY_DIR', 'PASS ZONE':'PASS_ZONE', 'DEF FRONT':'DEF_FRONT'})

#clean dataframe with only offensive plays
offense = data_df[data_df['ODK'] == 'O']
offense_df = offense[(offense['PLAY_TYPE'] == 'Run') | (offense['PLAY_TYPE'] == 'Pass')]

#makes space in between lines
def make_space():
  print(' ')

#finds run plays
def find_run(data):
  run_plays_df = data[data['PLAY_TYPE'] == 'Run']
  run_percentage = (100*len(run_plays_df)/len(data))
  print('Run: ', len(run_plays_df), 'plays,', round(run_percentage,2), '% of total')

#finds pass plays
def find_pass(data):
  pass_plays_df = data[data['PLAY_TYPE'] == 'Pass']
  pass_percentage = (100*len(pass_plays_df)/len(data))
  print('Pass: ', len(pass_plays_df), 'plays,', round(pass_percentage,2), '% of total')

#finds top 2 most used offensive formations
def top_formations(data):
  print('MOST USED FORMATIONS')
  most_used_formations = data['OFF_FORM'].value_counts().head(n=2)
  print(most_used_formations.to_string())

#finds least 2 used offensive formations
def least_used_formations(data):
  print('LEAST USED FORMATIONS')
  least_used_formations = data['OFF_FORM'].value_counts().tail(n=2)
  print(least_used_formations.to_string())

#finds most and least efficient formations
def formation_efficiencies(data):
  formation_efficiency = (data[['GN/LS', 'OFF_FORM']].copy())
  formation_list = list(zip(formation_efficiency['GN/LS'], formation_efficiency['OFF_FORM']))
  formation_dictionary = {}
  for elem in formation_list:
      if elem[1] in formation_dictionary:
          formation_dictionary[elem[1]].append(elem[0])
      else:
          formation_dictionary[elem[1]] = [elem[0]]
  formation_average = {}
  for i,j in formation_dictionary.items():
    formation_average[i] = round(sum(j)/ float(len(j)), 2)

  efficiencies = list(sorted(formation_average, key=formation_average.get, reverse=True))

  print("MOST EFFICIENT FORMATIONS")
  print(efficiencies[0], formation_average.get(efficiencies[0]), 'yd/f on', len(formation_dictionary[efficiencies[0]]), 'play(s)') 
  print(efficiencies[1], formation_average.get(efficiencies[1]), 'yd/f on', len(formation_dictionary[efficiencies[1]]), 'play(s)')
  print("LEAST EFFICIENT FORMATIONS")
  print(efficiencies[-1], formation_average.get(efficiencies[-1]), 'yd/f on', len(formation_dictionary[efficiencies[-1]]), 'play(s)')
  print(efficiencies[-2], formation_average.get(efficiencies[-2]), 'yd/f on', len(formation_dictionary[efficiencies[-2]]),'play(s)')

#finds quarter where team was most in red zone
def most_common_quarter(data):
  print('QUARTER(S) MOST IN ZONE')
  first_efficient = data['QTR'].value_counts().head(n=1)
  if len(((data['QTR'].value_counts()).to_frame())) > 1:
    print('QUARTER', first_efficient.to_string(), 'PLAYS')
    second_efficient = data['QTR'].value_counts().iloc[[1]]
    print('QUARTER', second_efficient.to_string(), 'PLAYS')
  else:
    print('QUARTER', first_efficient.to_string(), 'PLAYS')

#redzone part of report (1<=x<=20 yards)
def redzone():
  print('REDZONE')
  redzone_plays_df = offense_df[offense_df['YARD_LN'].between(1,20, inclusive='both')]
  find_run(redzone_plays_df)
  find_pass(redzone_plays_df)
  top_formations(redzone_plays_df)
  least_used_formations(redzone_plays_df)
  formation_efficiencies(redzone_plays_df)
  most_common_quarter(redzone_plays_df)
  print('*(quarters where team was most in the red zone)')
  make_space()

#midfield part of report (-20<=x<=20 yards)
def midfield():
  print('MIDFIELD')
  midfield_plays_df = offense_df[offense_df['YARD_LN'].between(-49, -21, inclusive='both') | offense_df['YARD_LN'].between(21, 50, inclusive='both')]
  find_run(midfield_plays_df)
  find_pass(midfield_plays_df)
  top_formations(midfield_plays_df)
  least_used_formations(midfield_plays_df)
  formation_efficiencies(midfield_plays_df)
  most_common_quarter(midfield_plays_df)
  print('*(quarters where team was most middle)')
  make_space()

#backed up part of report (-20<=x<=-1 yards)
def backed_up():
  print('BACKED UP')
  backedup_plays_df = offense_df[offense_df['YARD_LN'].between(-20,-1, inclusive='both')]
  find_run(backedup_plays_df)
  find_pass(backedup_plays_df)
  top_formations(backedup_plays_df)
  least_used_formations(backedup_plays_df)
  formation_efficiencies(backedup_plays_df)
  most_common_quarter(backedup_plays_df)
  print('*(quarters where team was most backed up)')
  make_space()

redzone()
midfield()
backed_up()

sys.stdout.close()