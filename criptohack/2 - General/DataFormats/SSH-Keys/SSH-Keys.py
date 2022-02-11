from Crypto.PublicKey import RSA

if __name__ == '__main__':
    with open('./bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'r') as f:
        key_file = f.read()
        print(f'SSH n = {RSA.importKey(key_file).n}')
