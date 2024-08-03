import math


def main(z):
    scob1 = (z**3) + 3*(z**2) + 1
    one = 63*math.log(scob1) + 33*((79*(z**3))**3)
    two = 77*(z**5)
    three = 34*(z**6) + (z**5)
    if (z < 125):
        return one
    elif (125 <= z) and (z < 167):
        return two
    else:
        return three


print(main(85))
print(main(59))


# ike.gabrielyan@yandex.ru