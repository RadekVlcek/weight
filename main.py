from weight import Weight
from graph import Graph

data_file = 'data.json'
w = Weight('data.json')
date = w.get_date()
months = w.months

while True:
    w.cls()
    w.show_records(date)

    print('___________________________________________________')
    print('a=add record; s=show records; g=show graph; q=quit')
    
    i = input('>> ').lower()

    # Add record
    if i == 'a':
        # w.cls()
        try:
            record = float(input('Add weight for today: '))
            w.add_record(record, date)
        except ValueError as e:
            print('Enter a number, not a string.')
    
    elif i == 's':
        for i in range(len(w.months)):
            print(f'{i+1}. {w.months[i]}')

        select_month = int(input('\nChoose month: '))
        w.show_records(date, select_month)

    elif i == 'g':
        g = Graph(data_file)
        g.show_graph(date)

    # Exit program
    elif i == 'q':
        print('Bye\n')
        break