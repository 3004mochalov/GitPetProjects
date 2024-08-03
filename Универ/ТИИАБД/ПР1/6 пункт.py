А = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
В = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']

result = {}

for i in range(len(В)):
    if В[i] in result:
        result[В[i]] += А[i]
    else:
        result[В[i]] = А[i]

print(result)