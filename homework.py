stats_list = [10, 20, 30, 40, 50]
def stats(data):
    if not data: return {'min': None, 'max': None, 'avg': None, 'sum': 0}
    minimum = data[0]
    maximum = data[0]
    total = 0
    
    for n in data:
        total += n
        
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n        
    avg = total / len(data)
    result = {"min":minimum, "max": maximum, "avg": avg, "sum":total}  
    return result
m = stats(stats_list)
print(m)

# # вторая задача 
# count_words = ("Привет мир привет Python мир мир")
# count = count_words.split()
# w = ()
# def count_w(data):
#     for n in data:
#         if n==:
#             print(n)
#         else:
#             n

# print(count_w(count))

# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))    
# c = 0
# def calc(a, b):

#     c = a - b
#     print("результат вычитание: ", c)
#     c = a + b
#     print("результат сложение: ", c)
#     c = a * b
#     print("результат умножение: ", c)
#     if a < b:
#         print("делить на ноль нельзя")
#     else:
#         c = a / b
#         print("результат деления: ", c)

# m = calc(a, b)
# print(m)


# -------------- Задача 4 ---------------
# mounth = int(input("Введите номер месяца: "))

# def season(month):
#     if month < 3 > 5:
#         print("сезон зима")
#     elif month < 2 > 5:
#         print("сезон весна")
#     elif month < 5 > 9:
#         print("cезон лето")
#     elif month < 9 > 12:
#         print("сезон осень")
#     else:
#         print("такого месяца нету")

# mesyac = season(mounth)
# print(mesyac)

# --------------- Задача 5 --------------

# age = int(input("введите возраст"))
# def safe_input(prompt, type_func):
    
# --------------- Задача 6 -------------

# parse_number = ("1, 2, abc, 3.5, , xyz, 10")

# not_number = 0
# def parse(data):
#     new_numbers = []
#     for item in data:
#         try:
#             number = float(item)
#             new_numbers.append(number)
#         except ValueError:
#             # not_number !=int(item)
#             # new_numbers.append(not_number)
#             print("это текстовые данные")
#     return new_numbers

# p = parse(parse_number)
# print(p)

#------------ Задача 7 --------------

