import codecs
from pwn import log

if __name__ == '__main__':
    cipher = 'cvpbPGS{arkg_gvzr_V\'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}'
    log.info(f'cipher = {cipher}')
    flag = codecs.encode(cipher, 'rot13')
    log.info(f'flag = {flag}')
