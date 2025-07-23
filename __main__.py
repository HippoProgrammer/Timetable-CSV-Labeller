import csv # import csv modules
from alive_progress import alive_bar # import progress bar functionality
from string import ascii_uppercase
from math import ceil
from unicodedata import normalize

print('Timetable CSV Generator')

weeks = [1,2]
days = [1,2,3,4,5]
periods = [1,2,3,4,5]

def week2str(day:int,week:int):
    day_str = {1:'MONDAY',2:'TUESDAY',3:'WEDNESDAY',4:'THURSDAY',5:'FRIDAY',6:'SATURDAY',7:'SUNDAY'}[day]
    week_str = ascii_uppercase[week-1]
    return f'{day_str} - WEEK {week_str}'

def week2strheading(day:int,week:int):
    day_str = {1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',7:'SUN'}[day]
    week_str = ascii_uppercase[week-1]
    return f'{week_str}-{day_str}'

sheets = dict()
file = input('Filename? (no .csv extension please) ')
no_weeks = int(input('Number of weeks in school year?'))
for day in days:
    for week in weeks:
        print(week2str(day,week))
        if not(week != weeks[0] and input('Same as previous week? (y/N) ').lower() == 'y'):
            week_data = dict()
            for period in periods:
                week_data[period] = normalize('NFKC',input(f'PERIOD {period}: ').strip())
        sheets[week2strheading(day,week)] = week_data
with alive_bar(6) as bar:
    with open(f'{file}.csv','w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        for row in range(6):
            row_list = []
            if row == 0:
                for week_header in list(sheets.keys()):
                    for col in range(ceil(no_weeks/2)):
                        row_list.append(week_header)
            else:
                for week_data in list(sheets.values()):
                    for col in range(ceil(no_weeks/2)):
                        row_list.append(week_data[row])
                    
            writer.writerow(row_list)
            bar()
            


