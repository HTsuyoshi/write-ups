def euler_totient(p: int, q: int):
    return (p-1)*(q-1)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = euler_totient(p=p, q=q)
print(f'phi = {phi}')
