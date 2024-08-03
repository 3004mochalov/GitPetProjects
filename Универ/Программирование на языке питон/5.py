import math


def main(z, y):
    itog = 0
    n = len(z) - 1
    for i in range(1, n + 2):
        chisl1 = y[n+1-i]**2
        chisl2 = z[n+1-i]
        chast1 = chisl1/27
        chast2 = chisl2/12
        itog = itog + abs(chast1 + chast2)**5
    return itog


print(main([-0.58, 0.35, 0.37, -0.09, 0.54, -0.71, -0.14], [0.16, -0.34, -0.77, 0.38, 0.9, 0.63, -0.08]))
print(main([0.42, 0.81, -0.68, -0.85, -0.57, -0.87, 0.13], [0.97, 0.29, 0.93, 0.76, 0.33, 0.17, 0.54]))
