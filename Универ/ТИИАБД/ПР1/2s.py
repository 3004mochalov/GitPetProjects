def register_users(n, queries):
    db = set()
    results = []

    for query in queries:
        if query not in db:
            db.add(query)
            results.append("OK")
        else:
            i = 1
            while f"{query}{i}" in db:
                i += 1
            new_name = f"{query}{i}"
            db.add(new_name)
            results.append(new_name)

    return results

# Пример использования
m = 0
while m < 3:
    n = int(input("Введите количество запросов: "))
    queries = []
    for _ in range(n):
        query = input("Введите запрос: ")
        queries.append(query)
    
    results = register_users(n, queries)
    
    for result in results:
        print(result)
    m +=1