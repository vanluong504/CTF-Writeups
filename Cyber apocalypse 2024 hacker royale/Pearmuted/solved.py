from Crypto.Util.number import *
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from hashlib import sha256
from data import g, A, B
from sage.all import*


a = 839949590738986464
b = 828039274502849303
class Permutationx:
    def __init__(self, mapping):
        self.length = len(mapping)

        assert set(mapping) == set(range(self.length))     # ensure it contains all numbers from 0 to length-1, with no repetitions
        self.mapping = list(mapping)

    def __call__(self, *args, **kwargs):
        idx, *_ = args
        assert idx in range(self.length)
        return self.mapping[idx]
    def __mul__(self, other):
        ans = []

        for i in range(self.length):
            ans.append(self(other(i)))

        return Permutationx(ans)

    def __pow__(self, power, modulo=None):
        ans = Permutationx.identity(self.length)
        ctr = self

        while power > 0:
            if power % 2 == 1:
                ans *= ctr
            ctr *= ctr
            power //= 2

        return ans

    def __str__(self):
        return str(self.mapping)

    def identity(length):
        return Permutationx(range(length))

g = Permutationx(g)
assert str(g**a) == str(A) and str(g**b) == str(B)

A, B = Permutationx(A), Permutationx(B)
C = A**b
assert C.mapping == (B**a).mapping

sec = tuple(C.mapping)
sec = hash(sec)
sec = long_to_bytes(sec)

hash = sha256()
hash.update(sec)

key = hash.digest()[16:32]
enc = b'\x89\xba1J\x9c\xfd\xe8\xd0\xe5A*\xa0\rq?!wg\xb0\x85\xeb\xce\x9f\x06\xcbG\x84O\xed\xdb\xcd\xc2\x188\x0cT\xa0\xaaH\x0c\x9e9\xe7\x9d@R\x9b\xbd'
iv = b"mg'g\xce\x08\xdbYN2\x89\xad\xedlY\xb9"

cipher = AES.new(key, AES.MODE_CBC, iv)
flag = unpad(cipher.decrypt(enc), 16).decode()
print(flag)