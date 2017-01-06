# Kamil Pek 231050
# 06.01.2017
# python elgamal.py
# -g generowanie liczby pierwszej i generatora, -k generowanie pary kluczy
# -e szyfrowanie, -d deszyfrowanie, -s podpisywanie, -v werfyikacja

import random
import math
import sys

def gcd( a, b ):
		if b != 0:
				return gcd( b, a % b )
		return a

def modexp( base, exp, modulus ):
		return pow(base, exp, modulus)

def mul_inv(a, b):
	    b0 = b
	    x0, x1 = 0, 1
	    if b == 1: return 1
	    while a > 1:
	        q = a / b
	        a, b = b, a%b
	        x0, x1 = x1 - q * x0, x0
	    if x1 < 0: x1 += b0
	    return x1

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

def encrypt(p, g, x, h, iNumBits, sPlaintext):
		z = encode(sPlaintext, iNumBits)
		cipher_pairs = []
		for i in z:
				y = random.randint( 0, p )
				c = modexp( g, y, p )
				d = (i*modexp( h, y, p)) % p
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

def siggen(p, g, x, m):
		while 1:
			k = random.randint(1,p-2)
			if gcd(k,p-1)==1: break
		r = pow(g,k,p)
		l = mul_inv(k, p-1)
		s = l*(m-x*r)%(p-1)
		return r,s

def sigver(p, a, y, r, s, m):
		if r < 1 or r > p-1 : return False
		v1 = pow(y,r,p)%p * pow(r,s,p)%p
		v2 = pow(a,m,p)
		return v1 == v2

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
			epub = open("public.txt", "r")
			for line in epub:
				if index == 2: pubkh = int(line)
				index = index + 1
			index = 0
			epriv = open("private.txt", "r")
			for line in epriv:
				if index == 0: privkp = int(line)
				if index == 1: privkg = int(line)
				if index == 2: privkx = int(line)
				index = index + 1
			iNumBits = 256
			eplain = open("plain.txt", "r")
			for line in eplain:
				message = str(line)
			cipher = encrypt(privkp, privkg, privkx, pubkh, iNumBits, message)
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
			decrypted = u''.join((decrypt(privkp, privkx, cipher))).encode('utf-8').strip()
			edecrypt = open("decrypt.txt", "w")
			edecrypt.write('%s' % (decrypted))

		if sys.argv[1] == "-s":
			index = 0
			epriv = open("private.txt", "r")
			for line in epriv:
				if index == 0: privkp = int(line)
				if index == 1: privkg = int(line)
				if index == 2: privkx = int(line)
				index = index + 1
			message = open("message.txt", "r")
			for line in message:
				content = int(line)
			rr, ss = siggen(privkp, privkg, privkx, content)
			signature = open("signature.txt", "w")
			signature.write('%s\n%s' % (str(rr), str(ss)))

		if sys.argv[1] == "-v":
			index = 0
			signature = open("signature.txt", "r")
			for line in signature:
				if index == 0: sigr = int(line)
				if index == 1: sigs = int(line)
				index = index + 1
			message = open("message.txt", "r")
			for line in message:
				content = int(line)
			index = 0
			epub = open("public.txt", "r")
			for line in epub:
				if index == 0: pubkp = int(line)
				if index == 1: pubkg = int(line)
				if index == 2: pubky = int(line)
				index = index + 1
			isvalid = sigver(pubkp, pubkg, pubky, sigr, sigs, content)
			verify = open("verify.txt", "w")
			verify.write('Weryfikacja: %s' % isvalid)
			print("Weryfikacja: %s" % isvalid)

main()
