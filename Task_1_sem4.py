# Задача 1. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
# 60 -> 2, 2, 3, 5

import math 

number = int(input("Введите число N:  "))
for i in range(2, int(math.sqrt(number)) + 1):
    while (number % i == 0):
        print(i)
        number //= i # убираем множитель из числа

if (number != 1):
    print(number)
