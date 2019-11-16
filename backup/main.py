import os
from weight import Weight

# Run init
w = Weight('.\data.json')

while True:
    os.system('clear')
    w.show_records()

    print('___________________________________________________')
    print('a=add record ; s=show history; g=show graph; q=quit')
    
    i = input('>> ')        

    # Add record
    if i == 'a' or i == 'A':
        os.system('clear')      
        try:
            record = float(input('Add weight for today: '))
            w.add_record(record)
        except ValueError as e:
            print('Enter a number, not a string.')
        
    # Show history
    elif i == 's' or i == 'S':
        pass

    # Exit program
    elif i == 'q' or i == 'Q':
        print('Bye\n')
        break