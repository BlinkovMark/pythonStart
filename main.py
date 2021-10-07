import math as m


# 26
# U = (ln(x^3 + y) - y^4) / (e^y + 5.4 * k^3)
def task_tw_six():
    k, x, y = 3, 12, 9
    rsl = (m.log((m.pow(x, 3) + y), m.e) - m.pow(y, 4)) / (m.pow(m.e, y) + 5.4 * m.pow(k, 3))
    print("Task #26")
    print(task_tw_six(rsl))
    print("")





# 15
# N = (m^2 + 2.8 * m + 0.355) / (cos2y + 3.6)
def task_fifteenth():
    a, x, y,  = 3, 5, 8
    # [10 sin (u) – 5 sin (3u) + sin (5u)] / 16
    hard_sin5x = ((10 * m.sin(x)) - (5 * m.sin(3 * x)) + m.sin(5 * x)) / 16
    rsl = (m.cos(m.pow(x, 3) + 6) - m.sin(y - a)) / ((m.log((m.pow(x, 4)), m.e)) - (2 * hard_sin5x))
    print("Task #15")
    print(rsl)
    print(hard_sin5x)
    print("")


task_fifteenth()


# P = (sin^3(x) + ln(2y + 3x)) / (t^e + √x)
def task_sixteen():
    t, x, y = 2, 5, 8
    # power reduction sin
    # sin^3(x) = (3 * sin(x) - sin(3 * x)) / 4
    sin3x = (3 * m.sin(x) - m.sin(3 * x)) / 4
    rsl = (sin3x + m.log((2 * y + 3 * x), m.e)) / (m.pow(t, m.e) + m.sqrt(x))
    print("Task #16")
    print(sin3x)
    print(rsl)
    print("")


task_sixteen()
