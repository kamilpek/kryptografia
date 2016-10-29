import sys

ciphertext = ""
plaintext = ""
key = [6,1,8,0,3,3,9,8,8,7,4]

def crypto(plain, key):
    if(plain == None or key == None):
        return None
    else:
        result = ord(plain) + key
        if(result <= ord('z')):
            return chr(result)
        else:
            return chr(result - 26)

def decrypto(cipher, key):
    if(cipher == None or key == None):
        return None
    else:
        result = ord(cipher) - key
        if(result >= ord('a')):
            return chr(result)
        else:
            return chr(result + 26)

def prepare():
    orig = open("orig.txt", "r")
    plain = open("plain.txt", "w")
    for line in orig:
        text = line.lower()
        text = text.replace(" ", "")
        plain.write(text)

def prettifyString(inp, text):
    for c in inp:
        if(c != None):
            text += str(c)
            # sys.stdout.write(c)
    text += str("\n")
    return text

def main():

    if sys.argv[1] == "-e":
        plain = open("plain.txt", "r")
        cryptow = open("crypto.txt", "w")
        for line in plain:
            tcr = prettifyString(map(crypto, line, key), plaintext)
            cryptow.write(tcr)
        plain.close()
        cryptow.close()
    elif sys.argv[1] == "-d":
        cryptor = open("crypto.txt", "r+")
        decrypt = open("decrypt.txt", "w")
        for line in cryptor:
            tdc = prettifyString(map(decrypto, line, key), ciphertext)
            decrypt.write(tdc)
        cryptor.close()
        decrypt.close()
    elif sys.argv[1] == "-p":
        prepare()
    elif sys.argv[1] == "-k":
        print("kryptoanaliza")
        print("pracujemy nad tym")
    else:
        print("wybierz poprawna opcje")

main()
