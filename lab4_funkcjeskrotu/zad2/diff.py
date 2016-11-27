import sys

def diff():
	hex1 = raw_input('Podaj pierwszy ciag bitow: ')
	hex2 = raw_input('Podaj drugi ciag bitow: ')

	bin1 = bin(int(hex1, 16))[2:]
	bin2 = bin(int(hex2, 16))[2:]

	dlugosc = len(bin1)
	roznica = ([x == y for (x, y) in zip(bin1, bin2)].count(False))
	procent = (float(roznica)/float(dlugosc))*100

	print "Liczba rozniacych sie bitow: %d z %d, procentowo: %2.f%%." % (roznica, dlugosc, procent)

diff()
