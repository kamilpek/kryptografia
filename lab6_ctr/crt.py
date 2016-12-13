# Kamil Pek 231050
# 13.12.2016
# python crt.py

import array

def gcd(a, b):
    while( b != 0):
        c = a%b
        a = b
        b = c
    return a

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

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

def main():
    i = x = y = 0
    mz = az = 1
    p = []
    b = []
    uklad = open("uklad.txt", "r")
    result = open("crt.txt", "w")
    for line in uklad:
        numbers = line.split()
        p.append(int(numbers[0]))
        b.append(int(numbers[1]))
        check = gcd(p[x], b[x])
        if(check != 1):
            print("Cyfry nie sa wzglednie pierwsze parami.\n");
            exit(1)
        mz *= b[x]
        x = x + 1
    az = chinese_remainder(b, p)
    result.write('%d %d' % (az, mz))

if __name__ == "__main__":
    main()
