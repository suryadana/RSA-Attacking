import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util.number import inverse
from fractions import gcd
import gmpy

# [+] Lagi bikin kunci, mohon tunggu...
# [+] N : 435112696024251740877832648799
# [+] e : 33446981368486267921397490881
# [+] Encrypted : 76805743480274074666775547847

# factordb.com
# p = 635666541859579
# q = 684498345235181

class Stack:
    def __init__(self):
        self.items = []
    def item(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def factor_pollard_rho(N):
    i = 1
    power = 2
    x = y = 2
    p = 1
    while p == 1:
        i += 1
        x = (x * x + 2) % N
        p = gcd(abs(x -y), N)
        if i == power:
            y = x
            power *= 2
    if p != N: 
        return p
    else:
        return None
def factor_fermat(N):
    a = gmpy.sqrt(N)
    b2 = a*a - N
    while not gmpy.is_square(gmpy.mpz(b2)):
        b2 += 2*a + 1
        a += 1

    factor1 = a - gmpy.sqrt(b2)
    factor2 = a + gmpy.sqrt(b2)
    return (long(factor1.digits()), long(factor2.digits()))

def calculate_privkey(p, q, e):
    phi = (p-1) * (q-1)
    d = inverse(e, phi)
    return d
def long_ascii_to_binary(M):
    tmp_flag = Stack()
    for i in str(M)[::-1]:
        tmp_flag.push(i)
    flag_assci = []
    while not tmp_flag.isEmpty():
        if int(tmp_flag.peek()) == 1:
            flag_assci.append(int(tmp_flag.pop()+tmp_flag.pop()+tmp_flag.pop()))
        elif int(tmp_flag.peek()) != 1:
            flag_assci.append(int(tmp_flag.pop()+tmp_flag.pop()))
    return ''.join(chr(x) for x in flag_assci)

def main():
    N = 435112696024251740877832648799
    e = 33446981368486267921397490881
    C = 76805743480274074666775547847
    p = 635666541859579
    q = 684498345235181
    d = calculate_privkey(p, q, e)
    M = pow(C, d, N)
    print long_ascii_to_binary(M)
        

if __name__ == '__main__':
    main()