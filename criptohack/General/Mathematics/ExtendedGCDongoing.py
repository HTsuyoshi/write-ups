import time

def egcd(a, b):
    x = 1
    y = 0
    x1, y1, a1, b1 = 0, 1, a, b

    while (b1 != 0):
        print(x, y)
        time.sleep(3)
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a, b1 = b1, a - q * b1

    return x, y

if __name__ == '__main__':
    p = 26513
    q = 32321
    a, b = egcd(p, q)
    print(a, b)
