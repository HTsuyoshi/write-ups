def egcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

if __name__ == '__main__':
    p = 26513
    q = 32321
    r, x1, x2 = egcd(p, q)
    print(f'x1 = {x1}, x2 = {x2}')
