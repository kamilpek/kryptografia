# Kryptografia i bezpieczeństwo systemów informatycznych
## Laboratorium 6. 11.12.2016

### Algorytm Euklidesa
Podstawowym algorytmem w arytmetyce modularnej jest algorytm Euklidesa znajdowania największego wspólnego dzielnika dwu liczb. Opiera się on na obserwacji, że NWD(a,b)=NWD(b,a%b) gdzie a%b jest resztą z dzielenia. Zakładamy tu, że a, b > 0. Z kolei NWD(a,0)=a.

Algorytm w wersji bardziej rozbudowanej (p. wykład 6, s. 10), może też zapamiętywać kombinację liniową a i b dającą bieżącą wartość reszty. Zaczynając od kombinacji liniowej a%b =1*a-(a/b)*b dojdzie do kombinacji NWD(a,b)=γ*a+β*b. Współczynniki γ i β nie są wyznaczone jednoznacznie, jeśli NWD(a,b)=γ*a+β*b, to również NWD(a,b)=(γ+b)*a+(β-a)*b. Pozwala to obliczyć współczynniki tak, by wybrany z nich był dodatni (oczywiście zawsze jeden jest dodatni, a drugi ujemny).

Jedna z interpretacji tego równania pozwala mówić o "odwrotności" liczby całkowitej, mianowicie jeśli NWD(a,n)=1 to równanie γ*a+β*n=1 oznacza, że γ*a=1 (mod n). Można założyć, że γ jest liczbą dodatnią.

### Algorytm Euklidesa c.d. – Chińskie twierdzenie o resztach
Wiemy, że dla liczb dodatnich m1 oraz m2 istnieją γ i β takie, że NWD(m1,m2)=γ*m1+β*m2. Załóżmy, że dany jest układ równań:
```
x=a1 (mod m1)
x=a2 (mod m2)
```
oraz, że NWD(m1,m2)=1. Wówczas γ*m1+β*m2=1. Sprawdzamy, że
```
x=a2*γ*m1+a1*β*m2
```
jest rozwiązaniem obu równań i jest jednoznaczne (mod m1*m2). Rozwiązanie dla dwóch równań można iterować dla większej ich liczby.

### Zadanie:

Program o nazwie crt czyta z pliku uklad.txt zawierającego pewną liczbę wierszy, każdy z wierszy jest parą liczb ai oraz mi, i= 1,2,...,k. Jeśli wszystkie liczby mi są dodatnie i parami względnie pierwsze, to program zapisuje w pliku crt.txt jeden wiersz składający się z liczb a0 i m0 takich, że m0=m1*...*mk oraz a0=ai (mod m0) dla i=1,2,...,k, 0≤a0<m0. W przeciwnym przypadku program informuje o błędzie.

Zadanie będzie testowane na pliku uklad.txt i powinno dać wynik crt.txt.
