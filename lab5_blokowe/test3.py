import commands

ca0 = "openssl "
cb0 = "dd if=letter-plain.bmp "

def imagencryptcbc():
    ccbca1 = "enc -aes-256-cbc -in letter-plain.bmp "
    ccbca2 = "-out letter-cbc.bmp -pass pass:mypass"
    ccbcb1 = "of=letter-bcb.bmp bs=1 count=54 conv=notrunc"
    commands.getoutput(ca0 + cbcba1 + cbcba2)
    commands.getoutput(cb0 + cbcbb1)

def imagencryptecb():
    cecba1 = "enc -aes-256-ecb -in letter-plain.bmp "
    cecba2 = "-out letter-ecb.bmp -pass pass:mypass"
    cecbb1 = "of=letter-ecb.bmp bs=1 count=54 conv=notrunc"
    commands.getoutput(ca0 + cecba1 + cecba2)
    commands.getoutput(cb0 + cecbb1)

def main():
    # imagencryptecb()
    imagencryptbcb()

if __name__ == "__main__":
    main()
