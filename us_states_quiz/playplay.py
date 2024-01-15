import pandas as pd

df = pd.read_csv('day-25-us-states-game-start/50_states.csv')
df['state'] = df['state'].str.lower()
state_list = df['state'].tolist()
# df = df.set_index('state')
# print(state_list)
print(df[df['state'] == 'ohio']['x'].iloc[0])
# print(df[df['state'] == 'ohio']['x'])
