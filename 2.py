f = open("file_2.txt", "r")
line_number = 0
for line in f:
    line = line.rstrip()
    print(f'Строка "{line}": {len(line.split())} слов')
    line_number += 1
print(f'Количество строк в файле - {line_number}')
f.close()