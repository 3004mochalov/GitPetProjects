import numpy as np
import matplotlib.pyplot as plt
import random

str1 = []
str2 = []
str3 = []
str4 = []
str5 = []


n = 0
while (n != 3):
    ran1 = random.randint(0, 1)
    ran2 = random.randint(0, 1)
    ran3 = random.randint(0, 1)
    ran4 = random.randint(0, 1)
    ran5 = random.randint(0, 1)
    str1.append(ran1)
    str2.append(ran2)
    str3.append(ran3)
    str4.append(ran4)
    str5.append(ran5)
    n += 1
str1.append(str1[1])
str1.append(str1[0])
str2.append(str2[1])
str2.append(str2[0])
str3.append(str3[1])
str3.append(str3[0])
str4.append(str4[1])
str4.append(str4[0])
str5.append(str5[1])
str5.append(str5[0])
figure = [str1, str2, str3, str4, str5]
fig, ax = plt.subplots()
ax.imshow(figure)
plt.show()gth=10, width=2)
ax.tick_params(which='minor', length=5, width=1)
plt.show()