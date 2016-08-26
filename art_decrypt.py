import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

def decyrpt(msg, privatekey):
    return privatekey.decrypt(msg)

def message1():
    print "Message 1 :\n"
    key1 = RSA.importKey(open('key1.pem','r').read())
    message1 = "message1_"
    for s in range(4):
        msg1 = open(message1+str(s), 'r')
        print str(s)+" >> ",decyrpt(msg1.read(), key1)

def message2():
    print "Message 2 :\n"
    key2 = RSA.importKey(open('key2.pem','r').read())
    message2 = "message2_"
    for i in range(4):
        msg2 = open(message2+str(i), 'r')
        print str(i)+" >> ",decyrpt(msg2.read(), key2)

def main():
    message1()
    message2()
if __name__ == '__main__':
    main()