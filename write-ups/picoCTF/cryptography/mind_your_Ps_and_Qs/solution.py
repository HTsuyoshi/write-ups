from factordb.factordb import FactorDB
from Crypto.Util.number import inverse, long_to_bytes
from pwn import log

if __name__ == '__main__':
    with open('values', 'r') as f:
        f.readline()
        c = int(f.readline().split(': ')[1])
        n = int(f.readline().split(': ')[1])
        e = int(f.readline().split(': ')[1])
    
    log.info(f'c = {c}')
    log.info(f'n = {n}')
    log.info(f'e = {e}')

    db = FactorDB(n)
    db.connect()

    p, q = db.get_factor_list()
    log.info(f'p = {p}')
    log.info(f'q = {q}')

    phi = (p-1)*(q-1)
    log.info(f'phi = {phi}')
    d = inverse(e, phi)
    flag = pow(c, d, n)
    log.info(f'flag = {long_to_bytes(flag)}')
