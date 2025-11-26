def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # Check which character types are missing
    missing_types = 0

    if not any(char in numbers for char in password):
        missing_types += 1
    if not any(char in lower_case for char in password):
        missing_types += 1
    if not any(char in upper_case for char in password):
        missing_types += 1
    if not any(char in special_characters for char in password):
        missing_types += 1

    # Minimum length requirement is 6
    missing_length = max(0, 6 - n)

    # The minimum characters to add is the max of missing types and missing length
    return max(missing_types, missing_length)

 
n = int(input())
password = input()
print(minimumNumber(n, password))
