# Написать функцию scramble, которая получает две строки и определяет: 
# можно ли из букв первой строки перестановкой получить второе слово.
#
# Примеры:
# scramble('rkqodlw', 'world') ==> True

import traceback



def scramble(s1, s2):
    c = list(s1)
    d = list(s2)
    r = len(d)
    q = 0
    for i in range(len(c)):
        for j in range(len(d)):
            if c[i]==d[j]:
                q = q + 1
                del d[j]
                break
               
    if r == q:
        return True
    else:
        return False


# Тесты
try:
    assert scramble('rkqodlw', 'world') ==  True
    assert scramble('cedewaraaossoqqyt', 'codewars') == True
    assert scramble('katas', 'steak') == False
    assert scramble('scriptjava', 'javascript') == True
    assert scramble('scriptingjava', 'javascript') == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
