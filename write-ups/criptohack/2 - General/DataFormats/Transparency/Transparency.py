from Crypto.PublicKey import RSA

if __name__ == '__main__':
    with open('./transparency_afff0345c6f99bf80eab5895458d8eab.pem', 'r') as f:
        key_file = f.read()
        print(RSA.importKey(key_file))
