def repeatedString(s, n):
    # count 'a' in one full string
    count_a = s.count('a')
    
    # how many full repeats of s fit in n
    full_repeats = n // len(s)
    
    # remainder characters
    remainder = n % len(s)
    
    # total 'a's = from full repeats + from remainder substring
    total_a = count_a * full_repeats + s[:remainder].count('a')
    
    return total_a


# -------- Main (HackerRank style) --------
s = input().strip()
n = int(input().strip())
print(repeatedString(s, n))
