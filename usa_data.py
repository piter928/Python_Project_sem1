import pandas as pd
import matplotlib.pyplot as plt

#Read data
df_Homicide_Race = pd.read_csv('C:/Users/xXx_420dankmeme_xXx/Desktop/PRG/python/Python_projekt/Homicide_Race_data.csv', sep=',')
df_Homicide_Age = pd.read_csv('C:/Users/xXx_420dankmeme_xXx/Desktop/PRG/python/Python_projekt/Homicide_Age_data.csv', sep=',')
#Data frame
df_Homicide_Race = pd.DataFrame(df_Homicide_Race)
df_Homicide_Age = pd.DataFrame(df_Homicide_Age)
#Column Homicide Race
names_Homicide_Race = df_Homicide_Race.iloc[:, 0] #Pierwsza kolumna
data_Homicide_Race = df_Homicide_Race.iloc[:, 1] #Druga kolumna
#Column Homicide Age
names_Homicide_Age = df_Homicide_Age.iloc[:, 0]
data_Homicide_Age = df_Homicide_Age.iloc[:, 1]

#===============Line chart homicide offenses================
df_Line_Chart = pd.read_csv('C:/Users/xXx_420dankmeme_xXx/Desktop/PRG/python/Python_projekt/DataLineChart.csv', sep=';')

df_Line_Chart = pd.DataFrame(df_Line_Chart)
Years = df_Line_Chart['series'].values
Years_Data = df_Line_Chart['United states'].values.astype(float)
fig0, ax0 = plt.subplots()
ax0.plot(Years, Years_Data, marker = 'o', linestyle = '-')
ax0.set_xlabel('Years')
ax0.set_ylabel('Rate per 100,000 people per year')
ax0.set_title('Rate of homicide offenses by population for years 2011-2021')
print(Years_Data)
#==================Line chart Age Data=======================
df_Race_Data = pd.read_csv('C:/Users/xXx_420dankmeme_xXx/Desktop/PRG/python/Python_projekt/PopulationAge2022.csv', sep=';')
df_Race_Data = pd.DataFrame(df_Race_Data)
df_Race_Data = df_Race_Data.dropna(axis=0)
age = df_Race_Data['Age'].values.astype(str)
age_percent = df_Race_Data['percent'].values.astype(float)
fig01, ax01 = plt.subplots()
ax01.bar(age, age_percent)
ax01.set_xlabel('Age')
ax01.set_ylabel('Percent')
ax01.set_title('Population by age in 2022 (population - 333,287,557)')
#==================Line chart Race Data=======================
df_Race_Data = pd.read_csv('C:/Users/xXx_420dankmeme_xXx/Desktop/PRG/python/Python_projekt/PopulationRace2022.csv', sep=';')
df_Race_Data = pd.DataFrame(df_Race_Data)
df_Race_Data = df_Race_Data.dropna(axis=0)
Race = df_Race_Data['Race'].values.astype(str)
Race_percent = df_Race_Data['percent'].values.astype(float)
fig02, ax02 = plt.subplots()
ax02.bar(Race, Race_percent)
ax02.set_xlabel('Race')
ax02.set_ylabel('Percent')
ax02.set_title('Population by race in 2022 (population - 333,287,557)')

fig1, ax1 = plt.subplots()
ax1.bar(names_Homicide_Race, data_Homicide_Race)
ax1.set_xlabel('Race')
ax1.set_ylabel('Number of offenders')
ax1.set_title('Homicide Race')

fig2, ax2 = plt.subplots()
ax2.bar(names_Homicide_Age, data_Homicide_Age)
ax2.set_xlabel('Age')
ax2.set_ylabel('Number of offenders')
ax2.set_title('Homicide Age')

plt.show()

"""df_Homicide_Race = pd.DataFrame(df_Homicide_Race)
df_Homicide_Race = df_Homicide_Race.apply(lambda x: x.astype(float) if x.name != 'key' else x)
column_homicide_race = df_Homicide_Race.filter(like='value')"""
#column_homicide_race_filtered = column_homicide_race[1:]


#print(column_homicide_race_filtered)