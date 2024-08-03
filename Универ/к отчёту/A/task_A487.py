# Написать функцию armstrong, которая возвращает заданное число в
# двоичной системе, если оно является числом Армстронга в десятичной системе
# или возвращает ноль, если это так. Число Армстронга - натуральное число,
# которое в данной системе счисления равно сумме своих цифр, возведённых
# в степень, равную количеству его цифр список из n
#
# Пример:
# 153 ==> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 ==> 10011001



import traceback


def armstrong(value):
    value_sum = 0
    t = value
    n = len(str(value))
    while value:
        value_sum += (value%10)**n
        value //= 10
    if value_sum != t:
        return 0
    else:
        b = bin(t)
        b1 = int (b[2::])
        return b1

# Тесты
try:
    assert armstrong(7) == 111
    assert armstrong(153) == 10011001
    assert armstrong(4887) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
