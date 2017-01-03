import random
import math
import sys

class PrivateKey(object):
	def __init__(self, p=None, g=None, x=None, iNumBits=0):
		self.p = p
		self.g = g
		self.x = x
		self.iNumBits = iNumBits

class PublicKey(object):
	def __init__(self, p=None, g=None, h=None, iNumBits=0):
		self.p = p
		self.g = g
		self.h = h
		self.iNumBits = iNumBits

def gcd( a, b ):
		if b != 0:
				return gcd( b, a % b )
		return a

def modexp( base, exp, modulus ):
		return pow(base, exp, modulus)

def SS( num, iConfidence ):
		for i in range(iConfidence):
				a = random.randint( 1, num-1 )
				if gcd( a, num ) > 1:
						return False
				if not jacobi( a, num ) % num == modexp ( a, (num-1)//2, num ):
						return False
		return True

def jacobi( a, n ):
		if a == 0:
				if n == 1: return 1
				else: return 0
		elif a == -1:
				if n % 2 == 0: return 1
				else: return -1
		elif a == 1: return 1
		elif a == 2:
				if n % 8 == 1 or n % 8 == 7: return 1
				elif n % 8 == 3 or n % 8 == 5: return -1
		elif a >= n: return jacobi( a%n, n)
		elif a%2 == 0: return jacobi(2, n)*jacobi(a//2, n)
		else:
				if a % 4 == 3 and n%4 == 3:	return -1 * jacobi( n, a)
				else: return jacobi(n, a )

def find_primitive_root( p ):
		if p == 2: return 1
		p1 = 2
		p2 = (p-1) // p1
		while( 1 ):
				g = random.randint( 2, p-1 )
				if not (modexp( g, (p-1)//p1, p ) == 1):
						if not modexp( g, (p-1)//p2, p ) == 1: return g

def find_prime(iNumBits, iConfidence):
		while(1):
				p = random.randint( 2**(iNumBits-2), 2**(iNumBits-1) )
				while( p % 2 == 0 ): p = random.randint(2**(iNumBits-2),2**(iNumBits-1))
				while( not SS(p, iConfidence) ):
						p = random.randint( 2**(iNumBits-2), 2**(iNumBits-1) )
						while( p % 2 == 0 ):
								p = random.randint(2**(iNumBits-2), 2**(iNumBits-1))

				p = p * 2 + 1
				if SS(p, iConfidence): return p

def encode(sPlaintext, iNumBits):
		byte_array = bytearray(sPlaintext, 'utf-16')
		z = []
		k = iNumBits//8
		j = -1 * k
		num = 0
		for i in range( len(byte_array) ):
				if i % k == 0:
						j += k
						num = 0
						z.append(0)
				z[j//k] += byte_array[i]*(2**(8*(i%k)))
		return z

def decode(aiPlaintext, iNumBits):
		bytes_array = []
		k = iNumBits//8
		for num in aiPlaintext:
				for i in range(k):
						temp = num
						for j in range(i+1, k):
								temp = temp % (2**(8*j))
						letter = temp // (2**(8*i))
						bytes_array.append(letter)
						num = num - (letter*(2**(8*i)))
		decodedText = bytearray(b for b in bytes_array).decode("utf-8", "ignore")
		return decodedText

def generate_keys(iNumBits=256, iConfidence=32):
		p = find_prime(iNumBits, iConfidence)
		g = find_primitive_root( p )
		x = random.randint( 1, p )
		h = modexp( g, x, p )
		publicKey = PublicKey(p, g, h, iNumBits)
		privateKey = PrivateKey(p, g, x, iNumBits)
		return {'privateKey': privateKey, 'publicKey': publicKey}

def encrypt(key, sPlaintext):
		z = encode(sPlaintext, key.iNumBits)
		cipher_pairs = []
		for i in z:
				y = random.randint( 0, key.p )
				c = modexp( key.g, y, key.p )
				d = (i*modexp( key.h, y, key.p)) % key.p
				cipher_pairs.append( [c, d] )

		encryptedStr = ""
		for pair in cipher_pairs:
				encryptedStr += str(pair[0]) + ' ' + str(pair[1]) + ' '

		return encryptedStr

def decrypt(keyp, keyx, cipher):
		plaintext = []
		cipherArray = cipher.split()
		if (not len(cipherArray) % 2 == 0):
				return "Malformed Cipher Text"
		for i in range(0, len(cipherArray), 2):
				c = int(cipherArray[i])
				d = int(cipherArray[i+1])
				s = modexp( c, keyx, keyp )
				plain = (d*modexp( s, keyp-2, keyp)) % keyp
				plaintext.append( plain )
		decryptedText = decode(plaintext, 256)
		decryptedText = "".join([ch for ch in decryptedText if ch != '\x00'])
		return decryptedText

def test():
		assert (sys.version_info >= (3,4))
		keys = generate_keys()
		priv = keys['privateKey']
		pub = keys['publicKey']
		message = "My name is Ryan."
		cipher = encrypt(pub, message)
		plain = decrypt(priv, cipher)

		return message == plain

def main():

		if sys.argv[1] == "-g":
			p = find_prime(256, 32)
			g = find_primitive_root(p)
			elg = open("elgamal.txt", "w")
			elg.write('%s\n%s' % (str(p), str(g)))

		if sys.argv[1] == "-k":
			index = 0
			elga = open("elgamal.txt", "r")
			for line in elga:
				if index == 0: p = int(line)
				elif index == 1: g = int(line)
				index = index + 1
			x = random.randint( 1, p )
			h = modexp( g, x, p )
			epriv = open("private.txt", "w")
			epriv.write('%s\n%s\n%s' % (str(p), str(g), str(x)))
			epub = open("public.txt", "w")
			epub.write('%s\n%s\n%s' % (str(p), str(g), str(h)))

		if sys.argv[1] == "-e":
			index = 0
			eplain = open("plain.txt", "r")
			epub = open("public.txt", "r")
			for line in epub:
				if index == 2: pubk = int(line)
				index = index + 1
			keys = generate_keys()
			pub = keys['publicKey']
			message = str(eplain)
			cipher = encrypt(pub, message)
			ecrypto = open("crypto.txt", "w")
			ecrypto.write('%s' % (str(cipher)))

		if sys.argv[1] == "-d":
			index = 0
			epriv = open("private.txt", "r")
			for line in epriv:
				if index == 0: privkp = int(line)
				if index == 2: privkx = int(line)
				index = index + 1
			ecrypt = open("crypto.txt", "r")
			for line in ecrypt:
				cipher = str(line)
			decrypted = decrypt(privkp, privkx, cipher)
			edecrypt = open("decrypt.txt", "w")
			edecrypt.write('%s' % (str(decrypted)))

		if sys.argv[1] == "-s":
			index = 0
			epriv = open("private.txt", "r")
			for line in epriv:
				if index == 0: privkp = int(line)
				if index == 1: privkg = int(line)
				if index == 2: privkx = int(line)
				index = index + 1
			message = open("message.txt", "r")
			k = random.randint( 1, privkp-1 )
			if gcd( k, privkp ) == 1: r = modexp(privkg, k, privkp)
			
main()
