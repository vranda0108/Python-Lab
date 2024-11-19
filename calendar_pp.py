day_names = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

def display_grid(d, row=5, col=7):
    c = ''
    c += ('.' + '-' * 5) * col + '.\n'
    c += ('|' + '  |'.join(day_names) + '  |').center(col * 7) + '\n'
    c += ('.' + '-' * 5) * col + '.\n'
    for i in range(row):
        c += '|'
        for j in range(col):
            c += f"{d[i][j]:^5}|"
        c += '\n'
        c += ('.' + '-' * 5) * col + '.\n'
    return c

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def cal_printer(mm=1, yy=2020):
    month_names = {1: 'January', 2: 'February', 3: 'March', 
                   4: 'April', 5: 'May', 6: 'June', 
                   7: 'July', 8: 'August', 9: 'September', 
                   10: 'October', 11: 'November', 12: 'December'}
    days_in_month = [31, 28 + is_leap_year(yy), 31, 30, 31, 30, 
                     31, 31, 30, 31, 30, 31]

    # Calculate the first day of the year
    day_of_week = (yy - 1 + (yy - 1) // 4 - (yy - 1) // 100 + (yy - 1) // 400) % 7
    
    # Adjust for the current month
    for m in range(mm - 1):
        day_of_week = (day_of_week + days_in_month[m]) % 7

    c = (month_names[mm] + ' ' + str(yy)).center(20, '-') + '\n'
    c += ' '.join(day_names) + '\n'

    # Print leading spaces for the first week
    c += '   ' * day_of_week
    for day in range(1, days_in_month[mm - 1] + 1):
        c += f"{day:2} "
        if (day_of_week + day) % 7 == 0:
            c += '\n'
    c += '\n'
    return c.strip()

def cal_printer_print(yy, fillchar='-'):
    calendars = [cal_printer(mm, yy).splitlines() for mm in range(1, 13)]
    formats = {
        '3X4': [(0, 3), (3, 6), (6, 9), (9, 12)],
        '4X3': [(0, 4), (4, 8), (8, 12)],
        '6X2': [(0, 6), (6, 12)],
        '12X1': [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
                 (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)],
    }

    x = input("Enter your Format (e.g., 3X4, 4X3, 6X2, 12X1): ").upper()
    if x not in formats:
        print("Invalid format!")
        return

    for group in formats[x]:
        for row in range(len(calendars[0])):
            print("   ".join(calendars[m][row] for m in range(*group)))
        print(fillchar * 70)

y = int(input("Enter your year: "))
z = input("Enter filler character: ")
cal_printer_print(y, fillchar=z)

