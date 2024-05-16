

# This file was *autogenerated* from the file solved2222.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_1 = Integer(1); _sage_const_25 = Integer(25); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_512 = Integer(512); _sage_const_16 = Integer(16); _sage_const_200 = Integer(200)
import random
import binascii

def coppersmith_short_pad(C1, C2, N, e = _sage_const_3 , eps = _sage_const_1 /_sage_const_25 ):
    P = PolynomialRing(Zmod(N), names=('x', 'y',)); (x, y,) = P._first_ngens(2)
    P2 = PolynomialRing(Zmod(N), names=('y',)); (y,) = P2._first_ngens(1)

    g1 = (x**e - C1).change_ring(P2)
    g2 = ((x + y)**e - C2).change_ring(P2)
 
    # Changes the base ring to Z_N[y] and finds resultant of g1 and g2 in x
    res = g1.resultant(g2, variable=x)

    # coppersmith's small_roots only works over univariate polynomial rings, so we 
    # convert the resulting polynomial to its univariate form and take the coefficients modulo N
    # Then we can call the sage's small_roots function and obtain the delta between m_1 and m_2.
    # Play around with these parameters: (epsilon, beta, X)
    roots = res.univariate_polynomial().change_ring(Zmod(N))        .small_roots(epsilon=eps)

    return roots[_sage_const_0 ]

def franklin_reiter(C1, C2, N, r, e=_sage_const_3 ):
    P = PolynomialRing(Zmod(N), names=('x',)); (x,) = P._first_ngens(1)
    equations = [x ** e - C1, (x + r) ** e - C2]
    g1, g2 = equations
    return -composite_gcd(g1,g2).coefficients()[_sage_const_0 ]


# I should implement something to divide the resulting message by some power of 2^i
def recover_message(C1, C2, N, e = _sage_const_3 ):
    delta = coppersmith_short_pad(C1, C2, N)
    recovered = franklin_reiter(C1, C2, N, delta)
    return recovered
    
def composite_gcd(g1,g2):
    return g1.monic() if g2 == _sage_const_0  else composite_gcd(g2, g1 % g2)

# Takes a long time for larger values and smaller epsilon
def test():
    N = random_prime(_sage_const_2 **_sage_const_512 , proof=False) * random_prime(_sage_const_2 **_sage_const_512 , proof=False)
    e = _sage_const_3 

    m = Integer(math.log(N, _sage_const_2 ) // e**_sage_const_2 )

    r1 = random.randint(_sage_const_1 , pow(_sage_const_2 , m))
    r2 = random.randint(_sage_const_1 , pow(_sage_const_2 , m))

    M = int(binascii.hexlify(b"hello"), _sage_const_16 )
    C1 = pow(pow(_sage_const_2 , m) * M + r1, e, N)
    C2 = pow(pow(_sage_const_2 , m) * M + r2, e, N)

    # Using eps = 1/125 is slooooowww
    print(coppersmith_short_pad(C1, C2, N, eps=_sage_const_1 /_sage_const_200 ))
    print(recover_message(C1, C2, N))

if __name__ == "__main__":
    test()

