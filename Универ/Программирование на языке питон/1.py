import math


def main(z, y):
    scob1 = ((z**3)/33) + (y**2) + 1
    chisl1 = 29*(scob1**5)
    scob2 = (y**2) + 60*(z**3) + 1
    znam1 = 60*math.pow(math.tan(scob2), 5)
    chast1 = chisl1/znam1
    scob3 = z - ((y**2)/16) - 16
    result = chast1 + (scob3**7)
    return result

main(-0.23, 0.29)
main(-0.88, 0.8)

#
# (math.tan())**5
# math.pow((math.tan(), 5)