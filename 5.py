numbers = [int(i) for i in input('Введите числа через пробел: ').split()]
with open("file_5.txt", "w") as f:
    print(*numbers, file=f)
print(f'Сумма чисел: {sum(numbers)}')