# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех книгах;
# – вывода информации о книге по введенному с клавиатуры номеру;
# – вывода количества книг, старше введённого года;
# – обновлении всей информации о книге по введенному номеру;
# – удалении книги по номеру.
# Провести тестирование функций.

library = [{"id" : "543", "title" : "Война и мир", "author" : "Толстой", "date" : "1873", "Genre" : "Epic novel"}, {"id" : "435", "title" : "Тихий дон", "author" : "Шолохов", "date" : "1889", "Genre" : "Epic novel"},{"id" : "344", "title" : "Капитанская дочка", "author" : "Пушкин", "date" : "1873", "Genre" : "Epic novel"},{"id" : "4", "title" : "На дне", "author" : "Горький", "date" : "1873", "Genre" : "Epic novel"},{"id" : "5", "title" : "Старуха Изергиль", "author" : "Горький", "date" : "1873", "Genre" : "Epic novel"},{"id" : "6", "title" : "Детство", "author" : "Горький", "date" : "1873", "Genre" : "Epic novel"},{"id" : "7", "title" : "Челкаш", "author" : "Горький", "date" : "1873", "Genre" : "Epic novel"},{"id" : "8", "title" : "Макар Чудра", "author" : "Горький", "date" : "1873", "Genre" : "Epic novel"},{"id" : "9", "title" : "Муму", "author" : "Тургенев", "date" : "1873", "Genre" : "Epic novel"},{"id" : "10", "title" : "Семья Вурдулака", "author" : "Тургенев", "date" : "1873", "Genre" : "Epic novel"}]
max_id = 0
for k in range (0, len(library)):
    if int ((library[k]["id"])) > max_id:
        max_id = int ((library[k]["id"])) 
def all_books():
    for k in range (0, len(library)):
        print ((library[k]["id"])+ (". ")+ (library[k]["title"])+ (" ") +(library[k]["author"])+ (" ")+ (library[k]["date"]) +(" ") +(library[k]["Genre"]))
def choice_book(n):
    if 0 <= n <= max_id:
        for k in range (0, max_id):
            if int ((library[k]["id"])) == n:
                print ((library[k]["id"])+ (". ")+ (library[k]["title"])+ (" ") +(library[k]["author"])+ (" ")+ (library[k]["date"]) +(" ") +(library[k]["Genre"]))
                break
    else:
        print (("book number incorrect") +(" or")+ (" not")+ (" exist!"))
def old_books(y):
    p = 0
    for k in range (0, len(library)):
        b = int((library[k]["date"]))
        if b < y:
            print ((library[k]["id"])+ (". ")+ (library[k]["title"])+ (" ") +(library[k]["author"])+ (" ")+ (library[k]["date"]) +(" ") +(library[k]["Genre"]))
            p += 1
    print (p)

def reset_book_info(r,t,a,d,g):
    for k in range (r-1, r):
        (library[k]["id"]) = str (r)
        (library[k]["title"]) = str (t)
        (library[k]["author"]) = str (a)
        (library[k]["date"]) = str (d)
        (library[k]["Genre"]) = str (g)
def delete_book_info(r):
    for k in range (0, len(library)):
        if library[k]["id"] == str (r):
            del library[k]
            break
