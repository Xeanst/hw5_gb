with open('file_6.txt', 'r') as f:
    for line in f:
        subject = line.split()[0]
        hours_number = 0
        hours = [line.split()[1], line.split()[2], line.split()[3]]
        for hour in hours:
            if hour != '—':
                hours_number += int(hour.split('(')[0])
        print(f'{subject} {hours_number} часов')
        hours_number = 0