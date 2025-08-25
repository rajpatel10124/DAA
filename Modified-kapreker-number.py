def kaprekarNumbers(p, q):
    kaprekar_list = []

    for n in range(p, q + 1):
        d = len(str(n))  # number of digits in n
        sq = n ** 2
        sq_str = str(sq)

        # Split the square into left and right parts
        r = sq_str[-d:]  # last d digits
        l = sq_str[:-d]  # remaining digits
        l = int(l) if l else 0
        r = int(r) if r else 0

        if l + r == n:
            kaprekar_list.append(n)

    if kaprekar_list:
        print(" ".join(map(str, kaprekar_list)))
    else:
        print("INVALID RANGE")


# HackerRank style input
if __name__ == "__main__":
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
