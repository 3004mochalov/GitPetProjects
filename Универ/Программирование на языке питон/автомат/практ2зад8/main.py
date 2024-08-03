from tkinter import *
import random
import rusyllab_space_free


def clicked():
    Name = ["Андрей", "Олег", "Никита", "Алексей"]
    FathName = ["Д.", "Г.", "М.", "О."]
    Surname = rusyllab_space_free.split_words(["Иванов", "Васильев", "Петров", "Смирнов", "Михайлов", "Фёдоров", "Соколов", "Яковлев", "Попов", "Андреев", "Алексеев", "Александров", "Лебедев", "Григорьев", "Степанов"])
    len_merge = 3
    while len(Name) != 0 and len(FathName) != 0 and len(Surname) != 0:
        random.shuffle(Surname)
        Surname[0: len_merge] = [''.join(Surname[0: len_merge])]
        a = random.randint(0, (len(Name)-1))
        b = random.randint(0, (len(FathName)-1))
        c = 0
        print((Name[a]) + " " + (FathName[b]) + " " + (Surname[c]))
        Name.pop(a)
        FathName.pop(b)
        Surname.pop(c)
    print(" ")

window = Tk()
window.title("NameGen")
window.geometry('400x250')
btn = Button(window, text="сгенерировать", command=clicked)
btn.grid(column=2, row=2)
window.mainloop()


#Источник: https://www.cyberforum.ru/python-beginners/thread2579652.html | https://github.com/Koziev/rusyllab/blob/master/rusyllab/rusyllab.py