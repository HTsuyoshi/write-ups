from Crypto.PublicKey import RSA

# At first convert .der to .pem
# Command:
# $ openssl x509 -inform DER -outform PEM -in 2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der -out key.pem


if __name__ == '__main__':
    with open('./key.pem', 'r') as f:
        key_file = f.read()
        print(f'n = {RSA.importKey(key_file).n}')
