from Crypto.Util.number import long_to_bytes

if __name__ == '__main__':
    n = 742449129124467073921545687640895127535705902454369756401331
    primes = qsieve(n)
    p, q = primes[0][0], primes[0][1]

    def euler_totient(p: int, q: int) -> int:
        return (p-1)*(q-1)

    phi = euler_totient(p, q)

    e = 3
    d = pow(e, -1, phi)

    ct = 39207274348578481322317340648475596807303160111338236677373

    def RSA(m: int, e: int, n: int) -> int:
        ring = Integers(n)
        cipher_text = ring(m) ** e
        return cipher_text

    plain_text = int(RSA(ct, d, n))
    plain_text = long_to_bytes(plain_text)

    print(f'plain_text = {plain_text}')
