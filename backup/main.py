from weight import Weight
from graph import Graph
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_date():
    from datetime import date

    d = date.today()
    months = ['January', 'February', 'March', 
            'April', 'May', 'June', 'July',
            'August', 'August', 'September',
            'October', 'November', 'December']

    # Return Day, Month, Year
    return [(d.day), months[d.month], d.year]

data_file_path = '.\data.json'
w = Weight(data_file_path)

while True:
    cls()
    w.show_records(get_date())

    print('___________________________________________________')
    print('a=add record ; g=show graph; q=quit')
    
    i = input('>> ')        

    # Add record
    if i == 'a' or i == 'A':
        cls()
        try:
            record = float(input('Add weight for today: '))
            w.add_record(record, get_date())
        except ValueError as e:
            print('Enter a number, not a string.')
        
    elif i == 'g' or i == 'G':
        g = Graph(data_file_path)
        g.show_graph()

    # Exit program
    elif i == 'q' or i == 'Q':
        print('Bye\n')
        break