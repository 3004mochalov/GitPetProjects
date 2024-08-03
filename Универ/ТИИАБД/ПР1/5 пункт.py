n = int(input())
sequence = []
for i in range(1, n+1):
    sequence += [i] * i
print(*sequence)