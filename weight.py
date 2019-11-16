class Weight():
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

    # Show records for current month
    def show_records(self, date):
        import json

        records = ''
        month, day = date[1], date[0]

        with open(self.data_file_path, 'r') as file:
            records = file.read()

            if records == '{}':
                print('\n --- NO RECORDS FOUND ---\n')
                return 0
        # File was closed at this point

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

    # Show records for all months 
    def show_history(self):
        pass

    # Add weight record
    def add_record(self, new_weight, date):
        import json
        import os

        day, month = str(date[0]), date[1]
        records = ''

        # Read from data file
        with open(self.data_file_path, 'r') as file:
            records = file.read()
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

        # os.system('clear')
        # self.show_records()