import pandas as pd
import matplotlib.pyplot as plt

#Python Project

#Read data
df_Homicide_Race = pd.read_csv('Homicide_Race_data.csv', sep=',')
df_Homicide_Age = pd.read_csv('Homicide_Age_data.csv', sep=',')
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
df_Line_Chart = pd.read_csv('DataLineChart.csv', sep=';')

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
df_Race_Data = pd.read_csv('PopulationAge2022.csv', sep=';')
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
df_Race_Data = pd.read_csv('PopulationRace2022.csv', sep=';')
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

#==================Rape Race Data=======================
df_Rape_Race = pd.read_csv('Offender_Race_05-28-2023_Rape.csv', sep=',')
df_Rape_Race = pd.DataFrame(df_Rape_Race)
names_Rape_Race = df_Rape_Race.iloc[:, 0] #Pierwsza kolumna
data_Rape_Race = df_Rape_Race.iloc[:, 1] #Druga kolumna

fig3, ax3 = plt.subplots()
ax3.bar(names_Rape_Race, data_Rape_Race)
ax3.set_xlabel('Race')
ax3.set_ylabel('Number of offenders')
ax3.set_title('Rape Race')

#==================Rape Age Data=======================
df_Rape_Age_Data = pd.read_csv('Offender_Age_05-28-2023_Rape.csv', sep=',')
df_Rape_Age = pd.DataFrame(df_Rape_Age_Data)
names_Rape_Age = df_Rape_Age.iloc[:, 0]
data_Rape_Age = df_Rape_Age.iloc[:, 1]

fig4, ax4 = plt.subplots()
ax4.bar(names_Rape_Age, data_Rape_Age)
ax4.set_xlabel('Age')
ax4.set_ylabel('Number of offenders')
ax4.set_title('Rape Age')

#==================Robbery Race Data======================

df_Robbery_Race_Data = pd.read_csv('Offender_Race_05-28-2023_Robbery.csv', sep=',')
df_Robbery_Race = pd.DataFrame(df_Robbery_Race_Data)
names_Robbery_Race = df_Robbery_Race.iloc[:, 0]
data_Robbery_Race = df_Robbery_Race.iloc[:, 1]

fig5, ax5 = plt.subplots()
ax5.bar(names_Robbery_Race, data_Robbery_Race)
ax5.set_xlabel('Race')
ax5.set_ylabel('Number of offenders')
ax5.set_title('Robbery Race')

#==================Robbery Age Data=======================

df_Robbery_Age_Data = pd.read_csv('Offender-Age_05-28-2023_Robbery.csv', sep=',')
df_Robbery_Age = pd.DataFrame(df_Robbery_Age_Data)
names_Robbery_Age = df_Robbery_Age.iloc[:, 0]
data_Robbery_Age = df_Robbery_Age.iloc[:, 1]

fig6, ax6 = plt.subplots()
ax6.bar(names_Robbery_Age, data_Robbery_Age)
ax6.set_xlabel('Age')
ax6.set_ylabel('Number of offenders')
ax6.set_title('Robbery Age')

#==================Aggravated Assault Age Data=======================

df_Assault_Age_Data = pd.read_csv('Offender-Age_05-28-2023_Aggravated_Assault.csv', sep=',')
df_Assault_Age = pd.DataFrame(df_Assault_Age_Data)
names_Assault_Age = df_Assault_Age.iloc[:, 0]
data_Assault_Age = df_Assault_Age.iloc[:, 1]
fig7, ax7 = plt.subplots()
ax7.bar(names_Assault_Age, data_Assault_Age)
ax7.set_xlabel('Age')
ax7.set_ylabel('Number of offenders')
ax7.set_title('Aggravated assault Age')

#==================Aggravated Assault Race Data=======================

df_Assault_Race_Data = pd.read_csv('Offender-Race_05-28-2023_Aggravated_Assault.csv', sep=',')
df_Assault_Race = pd.DataFrame(df_Assault_Race_Data)
names_Assault_Race = df_Assault_Race.iloc[:, 0]
data_Assault_Race = df_Assault_Race.iloc[:, 1]
fig8, ax8 = plt.subplots()
ax8.bar(names_Assault_Race, data_Assault_Race)
ax8.set_xlabel('Race')
ax8.set_ylabel('Number of offenders')
ax8.set_title('Aggravated assault Race')

plt.show()


