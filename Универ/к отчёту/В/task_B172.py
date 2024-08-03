# Написать функцию word_mesh, которая получает список строк и возвращает объединенную строку. 
# Слова в списке должны соединяться вместе, где одна или несколько букв в конце одного слова являются началом следующего слова в списке. 
# Но бывают случаи, когда все слова не совпадают. 
# Вернуть объединенную строку или "failed", если это невозможно.
#
# Примеры:
# word_mesh(["allow", "lowering", "ringmaster", "terror"]) ==> "lowringter" --> "low" + "ring" + "ter"

import traceback


def word_mesh(words):
    result = ''
    a = False
    for i in range(len(words)-1):
        first = words[i]
        second = words[i+1]
        for j in range(min(len(first), len(second)),-1,-1):
            if first[-j:] == second[:j]:
                result += first[-j:]
                break
            if j==0:
                a = True
    if a:
        return "failed"
    return result


# Тесты
try:
    assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
    assert word_mesh(["abcdef", "defghi", "xyz"]) == "failed"
    assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
    assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
    assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")