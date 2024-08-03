"""
1) Создать текстовый txt-файл.
2) Вставить туда англоязычную статью из Википедии.
3) Написать функцию со следующим функционалом:
3.1) Прочитать файл построчно, вывести на печать.
3.2) Создать список и добавить туда непустые строки.
3.3) В строках оставить только латинские буквы и пробелы. Прочие символы удалить.
3.4) Объединить список в единую строку. вывести на печать.
3.5) Подсчитать количество вхождений различных слов в тескте. Подсчет вести в словаре.
3.6) Вывести на печать 10 наиболее популярных и наименее популярных слов (“ 1) -- hello -- 15”).
3.7) Заменить наименее популярные слова на “PYTHON”.
3.8) Создать новый txt-файл.
3.9) Записать текст в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов и не делить слова.
"""

def wiki_function():
    f = open('text.txt', 'w')
    f.write("A p–n junction is a boundary or interface between two types of semiconductor materials,\n p-type and n-type, inside a single crystal of semiconductor. The (positive) side contains an excess of holes, while the (negative) side \ncontains an excess of electrons in the outer shells of the electrically neutral atoms there. \nThis allows electrical current to pass through the junction only in one direction. The p-n junction is created by doping, \nfor example by ion implantation, diffusion of dopants, or by epitaxy (growing a layer of crystal doped with one type of dopant on top of a layer of crystal \ndoped with another type of dopant). If two separate pieces of material were used, this would introduce a grain boundary between the semiconductors that would severely inhibit its\n utility by scattering the electrons and holes")
    f.close()
    f = open('text.txt', 'r')
    spisok = []
    for line in f:
        spisok.append(line)
        print(line, end= '')
    print(spisok)
    stroka = ''.join(spisok)
    print(stroka)
    m = 0
    s = {}
    a = stroka.split(' ')
    a = [i.replace('\n', '') for i in a]
    for i in a:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
        if s[i] > m:
            m = s[i]

    counter = 0
    leave = False
    print("TOP")
    while(True):
        for i in s:
            if s[i] == m:
                print(i)
                if i in a:
                    for p in range(len(a)):
                        if a[p] == i:
                            a[p] = 'python'
                            break
                counter += 1
            if counter == 10:
                leave = True
                break
        if leave:
            break
        m -= 1
    m = 1
    print("TOP NAOBOROT")
    counter = 0
    leave = False
    while(True):
        for i in s:
            if s[i] == m:
                print(i)
                counter += 1
            if counter == 10:
                leave = True
                break
        if leave:
            break
        m += 1
    f.close()
    f = open("new.txt", 'w')
    counter2 = 0
    print(a)
    for i in a:
        if counter2 + len(i) + 1 < 100:
            f.write(i + ' ')
            counter2 += len(i) + 1
        else:
            counter2 = len(i) + 1
            f.write('\n')
            f.write(i + ' ')
    f.close()
            
# Вызов функции
wiki_function()
