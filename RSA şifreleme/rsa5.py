import rsa
from rsa.key import PublicKey
from rsa.pkcs1 import verify

def generate_keys():
    (pubKey, privKey)=rsa.newkeys(1024)
    with open('keys/pubKey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('keys/privKey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

def load_keys():
    with open ('keys/pubKey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open ('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey , privKey

def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

def decrypt (Ciphertext, key):
    try:
        return rsa.decrypt(Ciphertext, key).decode('ascii')
    except:
        return False

def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

generate_keys()
PubKey,privKey = load_keys()

message = input('Enter a message:')
Ciphertext = encrypt(message, PubKey)

signature= sign_sha1(message, privKey)

plaintext= decrypt(Ciphertext, privKey)

print(f'Cipher text: {Ciphertext}')
print(f'Signature: {signature} ')

if plaintext:
    print(f'plain text: {plaintext} ')
else:
    print('could not decrypt the messaje.')

if verify_sha1(plaintext,signature, PubKey):

    print('signature verified!')

else:
    print('could not verify the messaje signature.')












    
