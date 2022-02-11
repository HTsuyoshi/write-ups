def RSA(m: int, e: int, p: int, q: int) -> int:
    n = p*q
    ring = Integers(n)
    cipher_text = ring(m) ** e
    return cipher_text

cipher_text = RSA(m=12, e=65537, p=17, q=23)
print(f'cipher_text = {cipher_text}')
