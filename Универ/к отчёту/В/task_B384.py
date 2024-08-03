# Написать функцию next_version, которая будет принимать строку (текущая версия программного обеспечения)
# и будет возвращать строку, содержащую следующий номер версии.
# Правила:
# все числа, кроме первого, должны быть меньше 10
# если после увеличения они становятся равными 10 - установите их в 0 и последовательно увеличите следующий номер
#
# Пример:
# next_version("1.2.3") ==> "1.2.4"
# next_version("0.9.9") ==> "1.0.0"

import traceback

def next_version(old):
    temp = old.split('.')
    temp = [int(i) for i in temp]
    temp = temp[::-1]
    temp[0] += 1
    for i in range(len(temp)):
        if temp[i] == 10 and i!=len(temp)-1:
            temp[i+1] += 1
            temp [i] = 0
    temp = [str(i) for i in temp[::-1]]        
    return '.'.join(temp)

# Тесты
try:
    assert next_version("1.2.3") == "1.2.4"
    assert next_version("0.9.9") == "1.0.0"
    assert next_version("1") == "2"
    assert next_version("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9"
    assert next_version("9.9") == "10.0"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
