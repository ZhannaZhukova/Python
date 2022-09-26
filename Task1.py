# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def DayIdenfity(dayNumber):
 if dayNumber == 6 or dayNumber == 7:
    print("Этот день выходной!")
 elif dayNumber > 0 and dayNumber < 6:
    print("Этот день рабочий!")
 elif dayNumber < 1 or dayNumber > 7:
    print("Вы ввели неправильный день!")


dayNumber = int(input('Введите номер дня: '))
DayIdenfity(dayNumber)