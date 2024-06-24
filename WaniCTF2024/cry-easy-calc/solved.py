import random
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Given values
p = 108159532265181242371960862176089900437183046655107822712736597793129430067645352619047923366465213553080964155205008757015024406041606723580700542617009651237415277095236385696694741342539811786180063943404300498027896890240121098409649537982185247548732754713793214557909539077228488668731016501718242238229
A = 60804426023059829529243916100868813693528686280274100232668009387292986893221484159514697867975996653561494260686110180269479231384753818873838897508257692444056934156009244570713404772622837916262561177765724587140931364577707149626116683828625211736898598854127868638686640564102372517526588283709560663960
ciphertext_hex = '9fb749ef7467a5aff04ec5c751e7dceca4f3386987f252a2fc14a8970ff097a81fcb1a8fbe173465eecb74fb1a843383'
ciphertext = bytes.fromhex(ciphertext_hex)

def f(s, p):
    u = 0
    for i in range(p):
        u += p - i
        u *= s
        u %= p
    return u

def encrypt(m: bytes, key: int) -> bytes:
    iv = os.urandom(16)
    key = long_to_bytes(key)
    key = md5(key).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return iv + cipher.encrypt(m)

def decrypt(ciphertext: bytes, key: int) -> bytes:
    iv = ciphertext[:16]
    key = long_to_bytes(key)
    key = md5(key).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return cipher.decrypt(ciphertext[16:])

# Brute force the value of s
for s in range(1, p):
    if f(s, p) == A:
        print(f"Found s: {s}")
        flag = decrypt(ciphertext, s)
        print(f"Decrypted flag: {flag}")
        break
else:
    print("s not found")