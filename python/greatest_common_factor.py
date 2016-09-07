""" 最大公约数 """


def greatest_common_factor(m, n):
    m, n = (m, n) if m > n else (n, m)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n


if __name__ == '__main__':
    m = 1200
    n = 1500
    r = greatest_common_factor(m, n)
    print(r)