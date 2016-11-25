import sys
import string

def diff():
	bity1 = raw_input('Podaj pierwszy ciag bitow: ')
	bity2 = raw_input('Podaj drugi ciag bitow: ')

	dlugosc = len(bity1)
	roznica = ([x == y for (x, y) in zip(bity1, bity2)].count(False))
	procent = (float(roznica)/float(dlugosc))*100

	print "Liczba rozniacych sie bitow: %d z %d, procentowo: %2.f." % (roznica, dlugosc, procent)

diff()
