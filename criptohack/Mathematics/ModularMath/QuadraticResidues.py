def quadratic_residue(x, p):
    for n in range(p):
        if (n * n) % p == x:
            print(n)
    return False

if __name__ == '__main__':
    p = 29
    ints = [14, 6, 11]

    for i in ints:
        quadratic_residue(i, p)
