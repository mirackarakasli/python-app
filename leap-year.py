#değişiklik yok
year = int(input("Please specify a year: "))
year = year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0
print("Is the year you have speficied LEAP YEAR? - ", year)
