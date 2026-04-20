year = int( input("vvedite god: "))

if year % 4 == 0 and year % 100 != 0:
    print("god vysokosnyi")
elif year % 400 == 0:
    print("god vysokosnyi")
else:
    print("year is not leap")
 