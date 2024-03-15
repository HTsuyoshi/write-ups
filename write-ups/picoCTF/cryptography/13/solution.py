from pwn import log

def ROT13(cipher):
    flag = ''
    for x in cipher:
        offset = ord('a')
        if x.isalpha():
            if x.isupper():
                offset = ord('A')
            flag += chr((ord(x) - offset + 13) % 26 + offset) 
        else:
            flag += x
    return flag

if __name__ == '__main__':
    log.info('Statement info:')
    cipher = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
    print(f'{cipher}')
    print(f'Flag = {ROT13(cipher)}')
