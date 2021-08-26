from pwn import *

if __name__ == '__main__':
    cypher = bytearray.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
    
    print (b64e(cypher))
