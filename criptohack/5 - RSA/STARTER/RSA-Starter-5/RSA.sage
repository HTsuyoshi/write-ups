def euler_totient(p: int, q: int) -> int:
    return (p-1)*(q-1)

def RSA(m: int, e: int, n: int) -> int:
    ring = Integers(n)
    c = ring(m)^e
    return c

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = euler_totient(p=p, q=q)

d = pow(e, -1, phi)

c = 77578995801157823671636298847186723593814843845525223303932
n = p*q
m = RSA(c, d, n)
print(f'm = {m}')
