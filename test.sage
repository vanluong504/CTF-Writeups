#!/usr/bin/env sage

from Crypto.Cipher import AES
from hashlib import sha256, sha512

F.<a> = GF(2^128, modulus=x^128 + x^7 + x^2 + x + 1)
P.<x> = PolynomialRing(F)

def bytes_to_poly(b):
    v = int.from_bytes(b, 'big')
    v = int(f"{v:0128b}"[::-1], 2)
    return F.fetch_int(v)

def poly_to_bytes(p):
    v = p.integer_representation()
    v = int(f"{v:0128b}"[::-1], 2)
    return v.to_bytes(16, 'big')

ct1 = bytes.fromhex('450abecfee723cdbe4393bbcf56add91e283615eaa6a5899906a138ce3dbe632ab778328029499c12eceefa0589945f7f3801748be3daa06ace2e682a77649da535f7235aa7ecb60bf0e3d6b7c1012e192411e29e6494c2fa05ce2c5d08d4698a05ffb5fa9ad2b2550737cea3b19ccacfdd93e7d3c3f6e641d5f')
ct2 = bytes.fromhex('450abecfee723cdbe4393bbce26a50c35bd4b250c5395150b62c27d76e20535dea6a129d08c1c31e89475b79d36e45f7f3801748be3daa06ace2e682a77649da535f7235aa7ecb60bf0e3d6b7c1012e192411e29e6494c2fa05ce2c5d08d4698a05ffb5fa9ad2b2550737cea3b19ccacfdd93e7d3c3f6e641d5f')
ct3 = bytes.fromhex('6fe550ba6db4b6a2af74f6f0454d82d959daa387f694685dec4c1ff7c36e40d3b9fe6e4fd41596035a594f8b599b89c47c84aa66d6d63ef3999de5041f0c3b7598b1811012399575a0c442c1c364f669ecf7fd5dfbb06bc37fd830c03e3dde20c98bc747d74d0ac196936f364c2e81338fca4bdb193d52e19f23')
tag1 = bytes.fromhex('8793b17261047b160c9acaf891577ef7')
tag2 = bytes.fromhex('1f668e1af6844a40e4cbdb6132cbd395')
tag3 = bytes.fromhex('295fc9e7546288a7464baa258fcd5542')

ct1 += b'\x00' * ((-len(ct1)) % 8)
ct2 += b'\x00' * ((-len(ct2)) % 8)
f = 0
for i in range(0, len(ct1), 16):
    f *= x
    f += bytes_to_poly(ct1[i:i + 16]) + bytes_to_poly(ct2[i:i + 16])
f *= x * x
f += bytes_to_poly(tag1) + bytes_to_poly(tag2)

for root, _ in f.roots():
    key1 = sha256(poly_to_bytes(root)).digest()
    dig = sha512(key1).digest()

    if dig[:16].hex() == 'ffd08593ad673b9005296a50f603af28':
        print("FOUND!!!")
        aeskey1 = dig[16:32]
        iv = bytes.fromhex('c336d16a10aac82969a59560')
        aad = bytes.fromhex('ffd08593ad673b9005296a50f603af28c336d16a10aac82969a59560bbbbbbbb')
        cipher = AES.new(aeskey1, AES.MODE_GCM, nonce=iv)
        cipher.update(aad)
        print(cipher.decrypt_and_verify(ct3, tag3))
