# import numpy as np

# weights = np.array([70, 85, 90, 65])
# # Твоя строка здесь:
# weights_g = weights * 100
# print (weights_g)

# import numpy as np
# heights = np.array([170, 155, 190, 165, 182, 150])
# tall = heights > 170
# result = heights[tall]
# print(result)

import numpy as np
# salaries = np.array([2000, 1500, 3500, 5000, 1200])
# sal_mean=salaries.mean()
# mean_hi = salaries > sal_mean
# print(salaries[mean_hi])
# print(sal_mean)

# data = np.array([
#     [80, 75], # Человек 1 (был 80, стал 75)
#     [95, 92], # Человек 2
#     [60, 61]  # Человек 3
# ])

# diff = data[:, 1] - data[:, 0]

# print(diff)
import numpy as np
# temps = np.array([
#     [15, 25, 5],
#     [18, 28, 2],
#     [20, 26, 8]
# ])

# # 1. Среднее в Сочи
# sochi_avg = temps[:, 1].mean()


# # 2. Жаркие дни во всех городах
# hot_values = temps > 20
# hot_values = temps[hot_values]

# print(f"Средняя в Сочи: {sochi_avg}")
# print(f"Значения выше 20: {hot_values}")

import pandas as pd # Стандартное сокращение

# data = [
#     {"Name": "Alice", "Age": 25, "City": "New York"},
#     {"Name": "Bob", "Age": 30, "City": "Paris"},
#     {"Name": "Charlie", "Age": 35, "City": "London"}
# ]

# df = pd.DataFrame(data)

# print(df)
# print(df.describe())

# import pandas as pd

# sales_data = {
#     "Product": ["Laptop", "Mouse", "Monitor", "Keyboard"],
#     "Amount": [1200, 25, 300, 80],
#     "Quantity": [5, 50, 10, 20]
# }

# # 1. Создай DataFrame
# df = pd.DataFrame(sales_data)
# print(df)
# # 2. Выдели колонку Amount
# amounts = df['Amount'].mean()
# print(amounts)

# # 1. Добавь колонку Total
# df['Total'] = df['Amount'] * df['Quantity']

# # 2. Создай новый DF с фильтром
# expensive_sales = df[df['Total']>1000]
# print(expensive_sales)
# df['Status'] = np.where(df['Total'] > 3000, 'VIP', 'Standard')

# print(df)

# Пример логики

# try:
#     number = int(data) # Тут Python споткнется
#     print("Успех!")    # Эта строка НЕ выполнится, если была ошибка
# except ValueError:
#     print("Это не число, пропускаем...") # Выполнится только при ошибке


# def proverka(datas):
#     new_data = []  # Создаем ПУСТОЙ СПИСОК до начала цикла [cite: 3, 46, 48]
    
#     for item in datas:
#         try:
#             # Пытаемся превратить элемент в число [cite: 27, 33, 49]
#             number = int(item) 
#             new_data.append(number) # Добавляем в список, если получилось [cite: 28, 46]
#         except ValueError:
#             # Если возникла ошибка (например, "ошибка"), просто идем к следующему элементу [cite: 34, 50]
#             continue 
            
#     # Блок вывода результата (условия if-else) [cite: 29, 38, 50]
#     if len(new_data) > 0:
#         total = sum(new_data) # Используем встроенную функцию sum() [cite: 44, 47]
#         print(f"Сумма: {total}") 
#     else:
#         print("Данных нет")

# data = [100, "200", 300, "ошибка", 500]
# proverka(data)


# def proverka(datas):
#     ages = []  # Используем список для хранения только ЧИСЕЛ (возрастов) [cite: 7, 56]
    
#     # Чтобы получить и имя, и возраст, используем .items()
#     for name, value in datas.items(): 
#         try:
#             age = int(value) # Пытаемся превратить значение в число [cite: 59]
#             ages.append(age) # Если успешно — добавляем в наш список [cite: 38]
#         except ValueError:
#             continue # Если там строка (как "отсутствовал") — просто пропускаем [cite: 70]
            
#     # Считаем результат после цикла [cite: 60]
#     if len(ages) > 0:
#         avg_age = sum(ages) / len(ages) # Сумма делить на количество элементов 
#         print(f"Средний возраст: {avg_age}")
#     else:
#         print("Данных нет")

# students = {'Ivan': 20, 'Oleg': 'отсутствовал', 'Dmitry': 18}
# proverka(students)

# data = [1, 2, 2, 3, 4, 4, 4, 5]

# 1. Превращаем список в множество (останутся только уникальные: 1, 2, 3, 4, 5)
# unique_data = set(data) 

# 2. Сравниваем длины (len) исходного списка и нового множества
# if len(unique_data) < len(data):
#     print("Были дубликаты")
# else:
#     print("Дубликатов нет")

# print(f"Очищенные данные: {unique_data}")

# def factorial(n):
#     # 1. Базовый случай: когда n равно 1, мы останавливаемся
#     if n == 1:
#         return 1
    
#     # 2. Рекурсивный шаг: умножаем текущее число на результат той же функции (n-1)
#     return n * factorial(n - 1)

# print(factorial(5)) 

# def factiorial(n):
#     if factiorial == 1:
#         return 1
#     else:
#         factiorial(n)= factiorial(n)-factiorial(n-1)
#         return factiorial
    
# print(factiorial(5))

# 1. Пишем сам декоратор
# def my_decorator(func):
#     def wrapper():
#         print("--- Начало работы ---") # Добавляем действие ДО
#         func()                         # Выполняем основную функцию
#         print("--- Конец работы ---")   # Добавляем действие ПОСЛЕ
#     return wrapper

# # 2. Используем "собачку" @ для применения
# @my_decorator
# def say_hello():
#     print("Привет, я учу Python!")

# say_hello()

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         avg = sum(self.grades)/ len(self.grades)
#         return avg

# # Создаем объект
# s1 = Student("Ivan", [5, 4, 5, 3])
# print(s1.average())

# class Monitor(Student): # В скобках указываем родителя
#     def __init__(self, name, grades, attendance):
#         # super() вызывает конструктор родителя, чтобы не дублировать код
#         super().__init__(name, grades) 
#         self.attendance = attendance # Свое новое свойство

#     def say_status(self):
#         print(f"Я староста {self.name}, моя посещаемость: {self.attendance}%")

# # Проверка:
# m1 = Monitor("Oleg", [5, 5, 4], 98)
# print(m1.average()) # Метод average() достался "по наследству"!
# m1.say_status()


# class DataModel:
#     def __init__(self):
#         # 1. Создаем приватный список при инициализации
#         self.__data = []

#     def add_value(self, value):
#         # 2. Пытаемся превратить входящее значение в число (float)
#         try:
#             numeric_value = float(value) 
#             self.__data.append(numeric_value)
#             print(f"Успешно добавлено: {numeric_value}")
#         # 3. Если float() выдал ошибку (например, на строку "abc")
#         except ValueError:
#             print(f"Ошибка типа данных: '{value}' не является числом")

#     # Добавим метод, чтобы посмотреть, что внутри (так как список приватный)
#     def show_data(self):
#         return self.__data

# # --- ПРОВЕРКА ---
# model = DataModel()

# model.add_value(10)          # Число
# model.add_value("20.5")      # Строка, которая может стать числом
# model.add_value("привет")    # "Грязная" информация (вызовет ошибку)

# print("Итоговый список:", model.show_data())

# def clean_names(data):
#     result = []
#     for item in data:
#         if  isinstance(item, str):
#             result.append(item)

#         else:
#             continue
#     return result


# srt = ["id", 100, "name", 3.14, "age", True]
# st = clean_names(srt)
# print(st)


# def convert_to_float(data):
#     result = []
#     for item in data:    
#         try:
#             value = float(item)
#             result.append(value)
#         except ValueError:
#             print(f"это мусор {item}")
#     return result

# srt = [170, "185.5", "ошибка", 190, "???"]
# st = convert_to_float(srt)
# print(st)

# def total_sales(data):
#     total = 0
#     # 1. Сразу берем только значения (500, "ошибка" и т.д.)
#     for value in data.values():
#         try:
#             # 2. Пытаемся превратить конкретное значение в число и прибавить
#             total += float(value)
#         except (ValueError, TypeError): 
#             # 3. Если это строка или что-то другое - пропускаем
#             print(f"Пропускаем некорректное значение: {value}")
#             continue
#     return total

sales = {"яблоки": 500, "бананы": "ошибка", "груши": 1200, "сливы": "нет данных"}
# print(f"Общая сумма продаж: {total_sales(sales)}")

# sales = {"яблоки": 500, "бананы": "ошибка", "груши": 1200, "сливы": "нет данных"}

# for name, price in sales.items():
#     if isinstance(price, int):
#         # Если проверка прошла, просто печатаем текущие name и price
#         print(f"У продукта {name} правильная цена: {price}")
#     else:
#         continue


# sales = {"яблоки": 500, "бананы": "ошибка", "груши": 1200, "сливы": "нет данных"}
# clean_sales = {} # 1. Создаем пустой словарь ДО цикла

# for name, price in sales.items():
#     if isinstance(price, int):
#         # 2. Добавляем новую пару в словарь: чистый_словарь[ключ] = значение
#         clean_sales[name] = price 

# print("Чистый словарь:", clean_sales) 
# # Выведет: {'яблоки': 500, 'груши': 1200}

salaries = {"Ivan": 500, "Oleg": "zero", "Anna": 1200, "Dmitry": "missing"}
valid_salaries = {}

salaries = {"Ivan": 500, "Oleg": "zero", "Anna": 1200, "Dmitry": "missing"}

# 1. Создаем пустую коробку
valid_salaries = {}

# 2. Запускаем конвейер
for name, price in salaries.items():
    try:
        # Используем ПРЯМО переменную price (не salaries.price!)
        value = float(price) 
        
        # Записываем в нашу коробку по имени сотрудника
        valid_salaries[name] = value
        print(f"Добавлено: {name} -> {value}")

    except ValueError:
        # Используем ПРЯМО переменную name
        print(f"Ошибка у сотрудника {name}")

# 3. Печатаем итог
print("---")
print("Итоговый чистый словарь:", valid_salaries)