import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_csv('C:\\Users\\lf.torres\\Downloads\\archive\\database.csv', index_col=0)

# 1. Listar las primeras cinco ciudades con el mayor numero de agencias
aux = df.groupby(['City'])['Agency Code'].unique()
agencies = aux.apply(lambda x: len(x))
agencies = agencies.sort_values(ascending = False)
print(agencies.head())

# 2. Listar los estados mas afectados por crimenes perpetrados por mujeres
crimes_by_women = df[df['Perpetrator Sex'] == 'Female']
states_most_affected = crimes_by_women['State'].value_counts().head()
print(states_most_affected)

# 3. Listar los estados mas afectados por crimenes perpetrados por hombres
crimes_by_men = df[df['Perpetrator Sex'] == 'Male']
states_most_affected = crimes_by_men['State'].value_counts().head()
print(states_most_affected)

# 4. Determinar el numero exacto del numero de crimenes hechos por mujeres de raza Asian/Pacific Islander
crimes_women_asian_pacific = df[(df['Perpetrator Sex'] == "Female") & (df['Perpetrator Race'] == 'Asian/Pacific Islander')]
number_crimes_women_asian_pacific = crimes_women_asian_pacific.shape[0]
print(number_crimes_women_asian_pacific)

# 5. Determinar el numero exacto de hispanos que han asesinado mediante la estrangulacion
hispanic_murders_by_strangulation = df[(df['Perpetrator Race'] == 'Hispanic') & (df['Weapon'] == 'Strangulation')]
number_hispanic_murders_by_strangulation = hispanic_murders_by_strangulation.shape[0]
print(number_hispanic_murders_by_strangulation)

# 6. Determinar el tipo de relacion mas peligrosa, el cual comete mas homicidios con arma de tipo Shotgun=escopeta
dangerous_relationship = df.groupby('Relationship')['Weapon'].apply(lambda x: (x == 'Shotgun').sum())
most_dangerous_relationship = dangerous_relationship.idxmax()
homicides_shotgun_most_dangerous_relationship = dangerous_relationship.max()
print(homicides_shotgun_most_dangerous_relationship)

# 7. Cual es el sexo que mas homicidios ha cometido con veneno = Poison
poison_homicides = df[df['Weapon'] == 'Poison']
gender_most_poison_homicides = poison_homicides['Perpetrator Sex'].value_counts()
most_poisonous_gender = gender_most_poison_homicides.idxmax()
homicides_by_most_poisonous_gender = gender_most_poison_homicides.max()
print("The gender that has committed the most homicides with poison is:", most_poisonous_gender)
print("Number of homicides committed by this gender with poison:", homicides_by_most_poisonous_gender)

# 8. Cuantos asesinos de raza negra atrapo el FBI
black_perpetrators_fbi_caught = df[(df['Perpetrator Race'] == 'Black') & (df['Crime Solved'] == 'Yes')]
num_black_perpetrators_fbi_caught = black_perpetrators_fbi_caught.shape[0]
print(num_black_perpetrators_fbi_caught)

# 9. Cual es el total de homicidios desde el año 1995 hasta el año 2000 perpetrado por hombres de raza negra por sofocacion = Suffocation
black_male_suffocation_1995_2000 = df[(df['Perpetrator Sex'] == 'Male') &
                                      (df['Perpetrator Race'] == 'Black') &
                                      (df['Weapon'] == 'Suffocation') &
                                      (df['Year'].between(1995, 2000))]
total = black_male_suffocation_1995_2000.shape[0]
print(total)

# 10. Determinar los homicidios de la policia municipal de la ciudad de new york del cual hayan sido por relaciones de tipo Ex-Wife, y ademas que su arma haya sido la estrangulacion = Strangulation
newyork_police_crimes = df[df['Agency Name'] == 'New York City Police Department']
newyork_police_exwife_strangulation_crimes = newyork_police_crimes[(newyork_police_crimes['Relationship'] == 'Ex-wife') &
                                                                   (newyork_police_crimes['Weapon'] == 'Strangulation')]
total = newyork_police_exwife_strangulation_crimes.shape[0]
print(total)
