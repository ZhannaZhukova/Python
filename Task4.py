#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

coordXPointA = int (input ('Введите координаты Х точки А: '))
coordYPointA = int (input ('Введите координаты Y точки А: '))
coordXPointB = int (input ('Введите координаты Х точки B: '))
coordYPointB = int (input ('Введите координаты Y точки B: '))

lenghtAB = sqrt (pow ((coordXPointA - coordXPointB),2) + pow ((coordYPointA-coordYPointB),2))

print (lenghtAB)