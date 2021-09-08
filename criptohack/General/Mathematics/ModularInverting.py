def mod_inv(i, m):
    for x in range(m):
        if ((i % m) * (x % m)) % m == 1:
            return x
if __name__ == '__main__':
    print(mod_inv(3, 13))
