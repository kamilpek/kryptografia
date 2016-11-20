import sys
import string

def main():
	checksums = open("hash.txt", "r+")
	hash1 = [128]
	hash2 = []
	i = 0
	for line in checksums:
		hash1[i] = line
		i+=1
	checksums.close()

main()
