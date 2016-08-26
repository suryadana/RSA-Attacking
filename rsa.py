from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from fractions import gcd
from base64 import b64decode

def read_pubkey(pem_file):
	pem = open(pem_file).read()
	key = RSA.importKey(pem)
	n = key.n
	e = key.e
	return (n,e)

n1,e1 = read_pubkey('pub1.key')
n2,e2 = read_pubkey('pub2.key')
print "n1 = ",n1
print "e1 = ",e1
print "\n"
print "n2 = ",n2
print "e2 = ",e2

