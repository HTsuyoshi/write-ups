def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

if __name__ == '__main__':
    a = 66528
    b = 52920
    print(gcd(a, b))
