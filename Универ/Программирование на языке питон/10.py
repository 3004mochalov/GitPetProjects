def main(data):
    res = []
    for i in range(len(data)):
        if data[i] not in res and data[i] != [None, None, None]:
            res.append(data[i])
    for i in range(len(res)):
        for j in range(len(res[i]) + 1):
            if j == 0:
                items = res[i][j].split(";")
                items[0] = str(round(float(items[0]), 1))
                fm = items[1].split(' ')
                items[1] = f'{fm[2]}, {fm[0][:1]}.{fm[1]}'
                res[i].pop(0)
                res[i].insert(0, items[1])
                res[i].insert(0, items[0])
            elif j == 2:
                res[i][2] = res[i][j][-7:]
            elif j == 3:
                # res[i][3] = res[i][j] == 'Y'
                res[i][3] = 'true' if res[i][j] == 'Y' else 'false'
    return res


print(main([[None, None, None], [None, None, None], ['0.62;Данила Е. Возов', '+76853027318', 'N'], ['0.55;Тихон Р. Мецацов', '+73988853083', 'Y'], ['0.62;Данила Е. Возов', '+76853027318', 'N'], ['0.62;Данила Е. Возов', '+76853027318', 'N'], ['0.39;Демид Р. Зучман', '+70123296833', 'N'], ['0.96;Макар З. Футман', '+70735430467', 'N']]))

