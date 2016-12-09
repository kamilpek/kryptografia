import commands
import sys
from os import popen

commands.getstatusoutput("openssl enc -aes-256-ecb -in letter-plain.bmp -out letter-ecb.bmp -pass pass:mypass")
commands.getstatusoutput("openssl enc -aes-256-cbc -in letter-plain.bmp -out letter-cbc.bmp -pass pass:mypass")

commands.getstatusoutput("dd if=letter-plain.bmp of=letter-ecb.bmp bs=1 count=54 conv=notrunc")
commands.getstatusoutput("dd if=letter-plain.bmp of=letter-cbc.bmp bs=1 count=54 conv=notrunc")
