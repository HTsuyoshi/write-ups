from pwn import *
from Crypto.Util.number import long_to_bytes
import json
import base64
import codecs

if __name__ == '__main__':
    r = remote('socket.cryptohack.org', 13377)

    def json_recv():
        line = r.recvline()
        return json.loads(line.decode())

    def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)

    stage = 0
    
    while stage < 100:
        received = json_recv()

        print('Received type:')
        print(received['type'])
        print('Received encoded value:')
        print(received['encoded'])

        encodingType = received['type']
        encodingValue = received['encoded']

        if encodingType == "base64":
            send = base64.b64decode(encodingValue.encode()).decode()

        elif encodingType == "hex":
            send = bytes.fromhex(encodingValue).decode()

        elif encodingType== "rot13":
            send = codecs.encode(encodingValue, 'rot_13')

        elif encodingType== "bigint":
            send = long_to_bytes(int(encodingValue.encode(), 16)).decode()

        elif encodingType == "utf-8":
            send = ''.join(chr(b) for b in encodingValue)

        print('Send value:')
        print(send)

        to_send = {
                'decoded': send
        }

        json_send(to_send)

        stage += 1
        print(stage)

    print(r.recvline())

