f = open('file_1.txt','w')
while True:
    s = input('Введите данные для записи в файл или нажмитее Enter для завершения ввода: ')
    if s == '': break
    f.write(s+'\n')
f.close()