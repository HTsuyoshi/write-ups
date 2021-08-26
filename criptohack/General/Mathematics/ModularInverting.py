def mod_inv(i, m):
    for x in range(m):
        if (i * x) % m == 1:
            return x

print(mod_inv(3, 13))
