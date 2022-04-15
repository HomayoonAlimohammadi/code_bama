day = int(input('Please enter the day: '))
month = int(input('Please enter the month: '))

if month <= 7:
    days_elapsed = ((month - 1) * 31) + day

else:
    days_elapsed = (6 * 31) + ((month - 6 - 1) * 30) + day

print(days_elapsed)