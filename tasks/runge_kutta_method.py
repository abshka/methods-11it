import math
from misc import runge_kutta

def runge_kutta_15():
    # Функция, описывающая правую часть дифференциального уравнения
    def f(x, y):
        return eval(equation)

    # Запрос дифференциального уравнения и начальных условий
    equation = input("Введите правую часть дифференциального уравнения в виде строки: ")
    x0 = float(input("Введите начальное значение аргумента: "))
    y0 = float(input("Введите начальное значение функции: "))

    # Запрос шага и числа итераций
    h = float(input("Введите шаг: "))
    n = int(input("Введите число итераций: "))

    # Вычисление решения дифференциального уравнения
    y = runge_kutta(x0, y0, h, n)

    # Вывод результата
    print("Решение дифференциального уравнения методом Рунге-Кутта: ", y)