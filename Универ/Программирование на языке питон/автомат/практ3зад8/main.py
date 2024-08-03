import numpy as np
import matplotlib.pyplot as plt
import random

m = 20
fig, ax = plt.subplots()
while m != 0:
    rx = random.randint(0, 100)
    ry = random.randint(0, 100)
    plt.scatter(rx, ry)
    plt.text(rx+.03, ry+.03, 'word', fontsize=10)
    m -= 1
plt.show()

