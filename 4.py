translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(translation[i[0]] + '  ' + i[1])
with open('file_3_new.txt', 'w') as f_new:
    f_new.writelines(new_file)