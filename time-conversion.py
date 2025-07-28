def timeConversion(s):
    period = s[-2:]          # AM or PM
    hour = int(s[:2])        # extract hour part
    
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    # format hour back to two digits with rest of the time
    return "{:02d}".format(hour) + s[2:-2]


# Input from user
s = input()
result = timeConversion(s)
print(result)
