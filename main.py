from math import log as ln


left, right = map(float, input("Введите границы:\n").split())
accuracy = float(input("Введите точность:\n"))  # 0.0001
delta = (right - left) / 10



def equation_solve(x):
    return (x ** 2 - 3 * x + x * ln(x)) # Вводим свое уравнение, при необходимости импортируем нужные модули



f_min, x_min, minimum_point = 0, 0, 0


def check(x_1, x_3, f_min, minimum_point, x_min):
    if (abs((f_min - equation_solve(minimum_point)) / equation_solve(minimum_point)) < accuracy and
            abs((x_min - minimum_point) / minimum_point) < accuracy):
        print("Функция достигает своего минимума в точке:",round(minimum_point, len(str(accuracy))))
        print("Значение функции в этой точке:", round(equation_solve(minimum_point), len(str(accuracy))))
    else:
        if x_1 < minimum_point < x_3:
            x_1 = min(x_min, minimum_point)
            x_2, x_3 = x_1 + delta, x_1 - delta
            f_1, f_2, f_3 = equation_solve(x_1), equation_solve(x_2), equation_solve(x_3)
            f_min = min(f_1, f_2, f_3)

            x_values = [x_1, x_2, x_3]
            x_min = x_values[[f_1, f_2, f_3].index(f_min)]
            try:
                minimum_point = (0.5 * (
                        (x_2 ** 2 - x_3 ** 2) * f_1 + (x_3 ** 2 - x_1 ** 2) * f_2 + (x_1 ** 2 - x_2 ** 2) * f_3)
                                 / ((x_2 - x_3) * f_1 + (x_3 - x_1) * f_2 + (x_1 - x_2) * f_3))
            except ZeroDivisionError:
                x_1 = x_min
                solver(x_1)
            check(x_1, f_min, minimum_point, x_min)
        else:
            x_1 = minimum_point
            solver(x_1)


def solver(x_1):
    global f_min, x_min, minimum_point
    f_1 = equation_solve(x_1)

    x_2 = x_1 + delta
    f_2 = equation_solve(x_2)

    x_3 = x_1 - delta if f_2 >= f_1 else x_1 + 2 * delta

    f_3 = equation_solve(x_3)

    f_min = min(f_1, f_2, f_3)
    x_values = [x_1, x_2, x_3]
    x_min = x_values[[f_1, f_2, f_3].index(f_min)]

    try:
        minimum_point = (0.5 * ((x_2 ** 2 - x_3 ** 2) * f_1 + (x_3 ** 2 - x_1 ** 2) * f_2 + (x_1 ** 2 - x_2 ** 2) * f_3)
                         / ((x_2 - x_3) * f_1 + (x_3 - x_1) * f_2 + (x_1 - x_2) * f_3))
    except ZeroDivisionError:
        x_1 = x_min
        solver(x_1)
    check(x_1, x_3, f_min, minimum_point, x_min)


x_1 = (right + left) / 2
solver(x_1)
