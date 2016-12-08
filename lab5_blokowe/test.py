import commands

commands.getoutput("openssl enc -aes-256-ecb -in letter-plain.bmp -out letter-ecb.bmp -pass pass:qwertyuiop")
commands.getoutput("openssl enc -aes-256-bcb -in letter-plain.bmp -out letter-bcb.bmp -pass pass:qwertyuiop")

commands.getoutput("dd if=letter-plain.bmp of=letter-ecb.bmp bs=1 count=54 conv=notrunc")
commands.getoutput("dd if=letter-plain.bmp of=letter-bcb.bmp bs=1 count=54 conv=notrunc")
