import json

class Weight():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

        try:
            file_exists = open(self.data_file_path)
        except FileNotFoundError:
            print(f'Created data file: {self.data_file_path}')
            with open(self.data_file_path, 'w') as new_data_file:
                new_data_file.write('{}')
        else:
            file_exists.close()

    def get_date(self):
        from datetime import date
        d = date.today()
        
        return [(d.day), self.months[d.month-1], d.year]

    def read_file(self, file):
        with open(file, 'r') as file:
            return file.read()

    # Show records for current month
    def show_records(self, date, select=0):
        records = {}
        day = date[0]

        month = date[1] if select == 0 else self.months[select-1]
        
        records = self.read_file(self.data_file_path)
        if records == '{}':
                print('\n --- NO RECORDS FOUND ---\n')
                return 0

        records = json.loads(records)

        print(f'\n\t| {month} |')
        print('\t------------------------------------')
        print(f'\t  DAY\t WEIGHT \t DIFFERENCE')
        
        if month in records:
            prev_weight = 0
            
            for day, weight in records[month].items():
                if day == 1 or day == 21 or day == 31:
                    day = f'{day}st'
                elif day == 2 or day == 22:
                    day = f'{day}nd'
                elif day == 3 or day == 23:
                    day = f'{day}rd'
                else:
                    day = f'{day}th'

                diff = weight - prev_weight

                if diff == weight:
                    diff = f' 0.0'
                else:
                    diff = format(diff, '.1f')
                    if float(diff) > 0.0:
                        diff = f'+{diff}'
                    elif float(diff) < 0.0:
                        diff = f'{diff}'
                    else:
                        diff = f' {diff}'

                # Store previous weight for comparison
                prev_weight = weight
                
                print(f'\t  {day}\t {weight} kg \t {diff}kg')
            print('\t------------------------------------\n')

    # Add weight record
    def add_record(self, new_weight, date):
        day, month = str(date[0]), date[1]
        records = {}

        # Read from data file
        records = self.read_file(self.data_file_path)
        records = json.loads(records)

        # Check if month exists
        if month in records:
            if day not in records[month]:
                records[month][day] = float(new_weight)
                print(f'Added record for today.')
            else:
                records[month][day] = float(new_weight)
                print(f'Record already existed for today and got overwritten.')

        # Create it if not
        else:
            records[month] = {}
            records[month][day] = float(new_weight)
            
        # Write back to data file
        with open(self.data_file_path, 'w') as file:
            file.write(json.dumps(records))