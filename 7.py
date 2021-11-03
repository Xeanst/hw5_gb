import json
profit = {}
pr = {}
profit_list = []
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль: {prof_aver}')
    else:
        print(f'Средняя прибыль отсуствует. Все работают в убыток')
    pr = {'average_profit': round(prof_aver)}
    profit_list.append(profit)
    profit_list.append(pr)
    print(f'Прибыль каждой компании: {profit_list}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit_list, write_js)
    js_str = json.dumps(profit_list)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')