import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('turbo_cars.csv')

# print(df.info)
# print(df.shape)
# print(df.describe())
# print(df.isnull().sum())
# print(df.isnull().mean()*100)
df = df.drop(columns=['specs_VIN',                      
                      'specs_Гос номер',
                      'specs_Комплектация',
                      'specs_Коробка передач',
                      'specs_Мощность',
                      'specs_Обмен',
                      'specs_Объем двигателя',
                      'specs_Пробег ( км )',
                      'specs_Прочее',
                      'specs_Рассрочка',
                      'specs_Тип топлива' ])

print("------------------------------------------")
# print(df.isnull().sum())
# print(df.isnull().mean()*100) #процент пропусков
# print(df.duplicated().sum()) # Дубликатов нету
# print(df.columns)
# print(df.describe())
print(df.info)
# print(df.shape)
# print(df.dtypes)
print("-----------------------------------")
# Меняю флоат типы на int
df['year_from_catalog'] = df['year_from_catalog'].astype('Int64')
df['millage_km'] = df['millage_km'].astype('Int64')
df['photos_count'] = df['photos_count'].astype('Int64')
df['specs_Год выпуска'] = df['specs_Год выпуска'].astype('Int64')
df[['specs_Кузов',
    'specs_Коробка',
    'specs_Наличие',
    'specs_Привод',
    'specs_Регион, город',
    'specs_Руль',
    'specs_Состояние',
    'specs_Таможня',
    'specs_Учёт']] = df[[
    'specs_Кузов',
    'specs_Коробка',
    'specs_Наличие',
    'specs_Привод',
    'specs_Регион, город',
    'specs_Руль',
    'specs_Состояние',
    'specs_Таможня',
    'specs_Учёт']].astype('category')

print(df.dtypes)
# print(df.head())
print(df.isnull().sum())
df['year_from_catalog'] = df['year_from_catalog'].fillna(df['year_from_catalog'].median())
df['millage_km'] = df['millage_km'].fillna(df['millage_km'].median())

# print(df.isnull().sum())