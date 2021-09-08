from Crypto.Util.number import GCD
from base64 import b64decode

if __name__ == '__main__':
    f = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')
    
    priv_key = f.read()[7:].replace('-----BEGIN RSA PRIVATE KEY-----', '').replace('-----END RSA PRIVATE KEY-----', '')
    
    print(int.from_bytes(b64decode(priv_key), 'big'))
