from Crypto.PublicKey import RSA

if __name__ == '__main__':
    with open('./privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as f:
        key_file = f.read()
        print(f'd = {RSA.importKey(key_file).d}')
