def euler_totient(p: int, q: int):
    return (p-1)*(q-1)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = euler_totient(p=p, q=q)

d = pow(e, -1, phi)
print(f'd = {d}')
