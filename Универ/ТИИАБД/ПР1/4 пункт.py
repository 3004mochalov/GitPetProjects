num = int(input("Введите число: "))
nums = [num]
while sum(nums) != 0:
    num = int(input("Введите число: "))
    nums.append(num)

squared_sum = sum([x*x for x in nums])
print("Сумма квадратов всех считанных чисел:", squared_sum)