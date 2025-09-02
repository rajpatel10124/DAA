def append_and_delete(s, t, k):
    common_length = 0   
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    total_operations = (len(s) - common_length) + (len(t) - common_length)
    if total_operations > k:
        return "No"
    elif (k - total_operations) % 2 == 0:
        return "Yes"
    elif len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"

s = input().strip()
t = input().strip()
k = int(input().strip())
print(append_and_delete(s, t, k))