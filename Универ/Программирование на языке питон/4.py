import math


def main(n):
    if n == 0:
        return 0.97
    elif n >= 1:
        chisl1 = math.sin(33*main(n-1))
        chisl2 = (math.tan(43*(main(n-1)**3)+main(n-1)+(main(n-1)**2)))**2
        chast1 = chisl1/70
        chast2 = chisl2/76
        return chast1-chast2


main(2)
main(6)
print(main(2))
print(main(6))