def libraryFine(d1, m1, y1, d2, m2, y2):
     if (y1, m1, d1) <= (y2, m2, d2):
        return 0

     if y1 > y2:
        return 10000

     if y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)

     
     if y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)

     return 0


# -------- Main code for HackerRank style input --------
if __name__ == "__main__":
    # First line: returned date
    d1, m1, y1 = map(int, input().split())
    # Second line: due date
    d2, m2, y2 = map(int, input().split())

    fine = libraryFine(d1, m1, y1, d2, m2, y2)
    print(fine)
