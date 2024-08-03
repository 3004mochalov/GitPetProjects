def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '//':
        result = num1 // num2
    elif operation == 'abs':
        result = abs(num1)
    elif operation == 'pow' or operation == '**':
        result = num1 ** num2
    else:
        result = None # Если операция неизвестна, результат будет None
    
    return result

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, /, //, abs, pow или **): ")

result = calculate(num1, num2, operation)
if result is None:
    print("Некорректная операция")
else:
    print("Результат:", result)