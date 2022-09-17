# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде 
# десятичной дроби.
# 0.001 -> 3.142
# 0.00001 -> 3.14159

from ast import Num
import math

def definition(n):
    d = int(math.log10(1 / x)) # возвращает десятичный логарифм числа
    return round(n, d)

num = float(input("Введите число ПИ: "))
x = float(input("Введите с какой точностью должно быть число:  "))
print(definition(num))

