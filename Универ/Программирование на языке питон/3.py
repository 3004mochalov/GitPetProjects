import math


def main(m, n, z):
    itog = 0
    for c in range(1, n+1):
        for i in range(1, m+1):
            scob1 = ((23*(z**3)) - 51 - (61*(z**2)))**5
            chast1 = scob1/2
            razn1 = chast1 - c
            itog = itog + (razn1 - (math.log10(i)**7))
    return itog
