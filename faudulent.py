def get_median(count, d):
    s = 0
    if d % 2 == 1:
        mid = d // 2 + 1
        for i in range(201):
            s += count[i]
            if s >= mid:
                return i
    else:
        mid1 = d // 2
        mid2 = mid1 + 1
        m1 = m2 = None

        for i in range(201):
            s += count[i]
            if m1 is None and s >= mid1:
                m1 = i
            if s >= mid2:
                m2 = i
                break
        return (m1 + m2) / 2


def activityNotifications(expenditure, d):
    count = [0] * 201
    n = len(expenditure)

    # Initialize frequency count with first d days
    for i in range(d):
        count[expenditure[i]] += 1

    notifications = 0

    # Process days from d to n-1
    for i in range(d, n):
        median = get_median(count, d)

        if expenditure[i] >= 2 * median:
            notifications += 1

        # Slide window:
        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications


 
n, d = map(int, input().split())
expenditure = list(map(int, input().split()))
print(activityNotifications(expenditure, d))
