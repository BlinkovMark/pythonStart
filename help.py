from math import *


S_tri, S_cir = int(input("Площадь треугольника: ")), int(input("Площадь круга: "))
action = int(input("Действие 1-Вписанная окружность 2-Описанная окружность: "))


def cir_in_tri():
    a = sqrt((4 * S_tri) / sqrt(3))
    r_max = (a * sqrt(3)) / 6
    r_cir = sqrt(S_cir / pi)
    print("a=", a, "r_max=", r_max, "r_cir", r_cir)
    if r_max >= r_cir:
        print("Вмещается")
    else:
        print("Не вмещается")


def tri_in_cir():
    a = sqrt((4 * S_tri) / sqrt(3))
    r_max = a * sqrt(3 / 3)
    r_cir = sqrt(S_cir / pi)
    print("a=", a, "r_max=", r_max, "r_cir", r_cir)
    if r_max >= r_cir:
        print("Вмещается")
    else:
        print("Не вмещается")


if action == 1:
    cir_in_tri()
else:
    tri_in_cir()
