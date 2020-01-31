from weight import Weight
from graph import Graph
import os

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def cls():
    os.system('cls') if os.name == 'nt' else os.system('clear')

w = Weight('data.json')
date = w.get_date()

while True:
    # cls()
    # w.show_records(date)

    print('___________________________________________________')
    print('a=add record; s=show records g=show graph; q=quit')
    
    i = input('>> ').lower()

    # Add record
    if i == 'a':
        # cls()
        try:
            record = float(input('Add weight for today: '))
            w.add_record(record, date)
        except ValueError as e:
            print('Enter a number, not a string.')
    
    elif i == 's':
        for i in range(len(months)):
            print(f'{i+1}. {months[i]}')

        select_month = int(input('Choose month: '))
        w.show_records(date, select_month)

    elif i == 'g':
        g = Graph(data_file_path)
        g.show_graph(date)

    # Exit program
    elif i == 'q':
        print('Bye\n')
        break