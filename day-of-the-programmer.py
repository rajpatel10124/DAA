def dayOfProgrammer(year):
    if year == 1918:
        # Transition year: Feb had 15 days skipped (Feb 14 was day 32)
        return "26.09.1918"
    elif (year < 1918 and year % 4 == 0) or \
         (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        # Leap year for Julian (before 1918) or Gregorian (after 1918)
        return f"12.09.{year}"
    else:
        # Normal year
        return f"13.09.{year}"

# Example usage
year = int(input().strip())
print(dayOfProgrammer(year))
