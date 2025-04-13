import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the csv file

df = pd.read_csv('Crime_Dataset.csv')  
print(df.head())
print(df.info())

# Data Cleaning and Preprocessing

df.columns = df.columns.str.strip().str.upper().str.replace(' ', '_')
df['DATE_OCC'] = pd.to_datetime(df['DATE_OCC'], errors='coerce')
df['YEAR'] = df['DATE_OCC'].dt.year
df['MONTH'] = df['DATE_OCC'].dt.month
df['HOUR'] = df['TIME_OCC'] // 100

df = df[(df['LAT'] != 0) & (df['LON'] != 0)]
df = df.drop_duplicates()
df = df[(df['VICT_AGE'] > 0) & (df['VICT_AGE'] < 100)]
df = df[df['VICT_SEX'].isin(['M', 'F', 'X'])]





# Crime by Hour

plt.figure(figsize=(10,5))
sns.countplot(x='HOUR', data=df)
plt.title("Crime Distribution by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Crimes")
plt.show()


# Top 10 Crime Types

top_crimes = df['CRM_CD_DESC'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(y=top_crimes.index, x=top_crimes.values)
plt.title("Top 10 Crime Types")
plt.xlabel("Number of Incidents")
plt.ylabel("Crime Type")
plt.tight_layout()
plt.show()

#   Weapon Usage Pattern
top_weapons = df['WEAPON_DESC'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(y=top_weapons.index, x=top_weapons.values)
plt.title("Top 10 Weapons Used")
plt.xlabel("Number of Crimes")
plt.ylabel("Weapon Type")
plt.tight_layout()
plt.show()

#  Victim Age Distribution

plt.figure(figsize=(10,5))
sns.histplot(df['VICT_AGE'], bins=30, kde=True, color='orange')
plt.title("Victim Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Plot - Victim Gender Distribution

plt.figure(figsize=(6,4))
sns.countplot(x='VICT_SEX', data=df, palette='Set2')
plt.title("Victim Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Area-wise Crime Count

if 'AREA_NAME' in df.columns:
    top_areas = df['AREA_NAME'].value_counts().head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_areas.values, y=top_areas.index)
    plt.title("Top 10 Areas with Most Crimes")
    plt.xlabel("Number of Crimes")
    plt.ylabel("Area")
    plt.show()

# Plot - Crimes Per Year

plt.figure(figsize=(10,5))
sns.countplot(x='YEAR', data=df, order=sorted(df['YEAR'].dropna().unique()))
plt.title("Crimes Per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Cleaned Data
df.to_csv('cleaned_crime_data.csv', index=False)

