#Kryptografia i bezpieczeństwo systemów informatycznych
## Laboratorium 2. 23.10.2016
Nadal zakładamy, że litery zakodowane są za pomocą liczb. Szyfr Vigenere'a jest właściwie zestawem szyfrów Cezara. Mianowicie, kluczem jest układ liczb k=<k0,k1,...,k(n−1)> zapamiętywany raczej w postaci liter. Kolejne litery tekstu jawnego szyfrowane (i odszyfrowywane) są przy pomocy szyfru Cezara z użyciem kolejnych liczb klucza. Dokładniej, jeśli x jest kolejną m-tą literą tekstu jawnego, a j=m mod n jest resztą z dzielenia m przez długość klucza n, to E(k,x)=x+kj, D(k,y)=y-kj.

Kryptoanaliza jest trywialna w przypadku znajomości długości klucza, tzn. n, oraz znajomości co najmniej n par tekstu jawnego i zaszyfrowanego. Jednakże w przypadku, gdy znany jest tylko szyfrogram, przeszukiwanie wyczerpujące traci sens, przestrzeń kluczy ma rozmiar 26n i jest za duża nawet dla niewielkich wartości n.  Stosowana jest w tym przypadku analiza częstotliwości.

Niech W będzie wektorem częstotliwości występowania poszczególnych liter w języku naturalnym. Dla języka angielskiego są to następujące liczby (w promilach)

82, 15, 28, 43, 127, 22, 20, 61, 70, 2, 8, 40, 24, 67, 75, 29, 1, 60, 63, 91, 28, 10, 23, 1, 20, 1
 a,  b,  c,  d,   e,  f,  g,  h,  i, j, k,  l,  m,  n,  o,  p, q,  r,  s,  t,  u,  v,  w, x,  y, z
Dla każdego wektora V o długości n i dla każdej liczby j=0,1,..,n-1, przez Vj oznaczamy wektor przesunięty, tzn. taki, że Vj[i]=V[i-j mod n], (w szczególności V=V0). Iloczyn skalarny dwóch wektorów V oraz U to suma V[0]*U[0]+V[1]*U[1]+...+V[n-1]*U[n-1].

Stwierdzenie: Dla dowolnego wektora V iloczyn skalarny Vj oraz Vi zależy tylko do różnicy j-i i jest największy gdy j=i. Dla podanego wyżej wektora W*W=0,066. Iloczyny skalarne (w promilach) dla poszczególnych przesunięć wynoszą:

66, 40, 31, 35, 45, 32, 33, 39, 34, 33, 37, 47, 39, 42, 39, 46, 37, 34, 34, 38, 35, 32, 45, 35, 32, 40
 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
tzn. maksymalna wielkość W*Wj dla j>0 wynosi 0,047, a średnia wielkość W*Wj dla j>0 wynosi 0,037 (wielkości są przybliżone).

Stwierdzenie: Jeśli dane są dwa losowe teksty języka naturalnego, to prawdopodobieństwo, że na identycznych pozycjach znajdują się identyczne litery wynosi W*W=0,066. (Dowód: dla ustalonej pozycji prawdopodobieństwo, że w drugim tekście występuje np. "a" pod warunkiem, że w pierwszym występuje "a" jest takie, jak bez tego założenia -- niezależność zdarzeń. Więc koincydencja litery "a" występuje z prawdopodobieństwem W[0]*W[0]. Jeśli uwzględnić cały alfabet, to otrzymana suma jest właśnie iloczynem skalarnym wektorów).

Przy pomocy tych narzędzi można opisać dwa kroki kryptoanalizy szyfru Vigenere'a bez znajomości tekstu jawnego.

Krok 1: Trzeba znaleźć długość klucza. W tym celu dla kolejnych liczb j=1,2,... dokonujemy przesunięcia tekstu zaszyfrowanego o j pozycji i obliczamy ile liter w obu tekstach, oryginalnym i przesuniętym, jest identycznych na tych samych pozycjach. Dla niektórych z tych przesunięć liczba koincydencji będzie znacząco większa. Jest to wielokrotność długości klucza. Oznaczmy najmniejszą taką liczbę przez n. W zasadzie powinniśmy zacząć próbować przesunięcia większe od co najmniej 4, dla mniejszych przesunięć trudno mówić o niezależności zdarzeń pojawienia się litery na jakiejś pozycji.

Krok 2: Dla każdego i=0,1,...,n-1 wydzielamy część kryptogramu na pozycjach o numerach równych i modulo n. Dla takiej części obliczamy wektor V częstotliwości występowania poszczególnych liter w kryptogramie. Zakładamy milcząco, że wektor ten jest zbliżony do wektora W z pewnym przesunięciem. Przesunięcie to będzie kluczem szyfru Cezara na rozpatrywanej pozycji. A znalezione będzie poprzez obliczenie iloczynów skalarnych wektora V z wektorami Wj, j=0,1,..,25. Jeden z tych iloczynów powinien być znacząco większy od pozostałych, dla tego przesunięcia j, ki = j.

###Zadanie:

Zaprogramować szyfrowanie i odszyfrowywanie wiadomości przy użyciu szyfru Vigenere'a. Zakładamy, że tekst jawny jest ciągiem małych liter bez spacji, cyfr i znaków przestankowych. Taki tekst jawny trzeba przygotować z realnie dostępnego tekstu za pomocą odpowiedniego narzędzia.

Program o nazwie vigenere powinien umożliwiać wywołanie z linijki rozkazowej z następującymi opcjami:

-p (przygotowanie tekstu jawnego do szyfrowania),
-e (szyfrowanie),
-d (odszyfrowywanie),
-k (kryptoanaliza wyłącznie w oparciu o kryptogram)

Nazwy tych plików są identyczne jak w poprzednim zadaniu:

plain.txt: plik z tekstem jawnym,
crypto.txt: plik z tekstem zaszyfrowanym,
decrypt.txt: plik z tekstem odszyfrowanym,
key.txt: plik zawierający klucz,
orig.txt: oryginalny tekst, przed przygotowaniem do szyfrowania
key-crypto.txt: plik z kluczem znalezionym w wyniku kryptoanalizy

Treścią zadania jest w zasadzie kryptoanaliza. Nie należy oczekiwać zadowalających wyników jeśli kryptogramy są krótkie. Jednak teksty języka naturalnego o długości setek i więcej znaków, np. zaszyfrowane artykuły prasowe, dadzą się rutynowo odszyfrować bez znajomości klucza.


