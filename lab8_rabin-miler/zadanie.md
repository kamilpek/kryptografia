# Kryptografia i bezpieczeństwo systemów informatycznych
## Laboratorium 8. 18.12.2016
### Algorytm Rabina-Millera (test pierwszości i rozkład na czynniki pierwsze)

Jedną z metod testowania pierwszości liczby jest próba rozkładu na czynniki. Ale dla dużych liczb metoda ta musi zawieść. Właśnie trudność rozkładu dużych liczb jest podstawą algorytmów kryptografii asymetrycznej. Istnieją jednak skuteczne testy pierwszości, wystarczająco wiarygodne dla zastosowań. Czasami dają one rozkład na czynniki pierwsze, a czasami nie.

Algorytm Rabina-Millera opiera się na dwóch twierdzeniach:

1. Twierdzenie Fermata: jeśli liczba n jest pierwsza, to an−1 = 1 (mod n).

Dowód: Iloczyn wszystkich liczb mniejszych niż n to n! Ale jeśli wszystkie liczby pomnożymy przez a, to otrzymamy ten sam zbiór liczb, a ma odwrotność, mnożenie przez a jest odwracalne. A więc n! = n!*an−1 (mod n).

Jeśli an−1 = 1 (mod n), to liczbę n nazywamy pseudopierwszą przy podstawie a, zaś liczbę a nazywamy świadkiem pierwszości liczby n.

Liczby Carmichaela są to liczby, które mają komplet świadków pierwszości, takich liczb jest naprawdę bardzo mało. Ale dla pozostałych liczb złożonych co najmniej połowa liczb a, 1<a<n, nie jest świadkiem pierwszości.

Wniosek: Wybieramy a, sprawdzamy, czy a ma wspólny dzielnik z n. Jeśli nie ma, to sprawdzamy, czy jest świadkiem pierwszości. Jeśli jest świadkiem, to testujemy kolejnego kandydata a. Jeśli kilkadziesiąt razy kolejny kandydat spełni równość, to jest mało prawdopodobne, by liczba n była złożona. Ale każdy nie-świadek jest dowodem, że liczba n jest złożona i dalsze testowanie przerywamy. Ale rozkładu nie znamy.

2. Jeśli a2 = b2 (mod n), to albo a = ±b (mod n), albo NWD(a−b,n) jest nietrywialnym dzielnikiem liczby n.

Dowód: a2−b2 = (a+b)*(a−b). Skoro (a+b)*(a−b) = 0 (mod n), to albo jeden z czynników jest równy zero, albo mamy rozkład liczby n.

Algorytm Rabina-Millera sprawdzania pierwszości liczby n działa następująco:

1. wybieramy dowolne a, 1<a<n, sprawdzamy, czy przypadkiem NWD(a,n) nie daje rozkładu.

2. stosujemy algorytm szybkiego potęgowania do obliczenia an−1 (mod n), ale w tej wersji, że na koniec pozostawiamy podnoszenie do kwadratu. Tzn. n−1 = m*2k, m nieparzyste, b0 = am (mod n), bj+1 = bj2 (mod n). Jeśli bk ≠ 1, to test Fermata wykazał złożoność. Jeśli bk = 1, to szukamy najwcześniejszego bj+1 = 1. Jeśli teraz bj ≠ −1, to mamy nietrywialną równość kwadratów dającą rozkład liczby n. Dokładniej, skoro (bj+1)*(bj-1)=0 (mod n), to NWD(bj-1,n) oraz NWD(bj+1,n) są nietrywialnymi dzielnikami n. Ale jeśli bj = −1, to n będzie silnie pseudopierwszą przy podstawie a. Podobnie, jeśli b0 = ±1. Wówczas powtarzamy krok 1.

3. Jeśli wielokrotnie okaże się, że n jest liczbą silnie pseudopierwszą, to przyjmujemy, że jest liczbą pierwszą. Prawdpodobieństwo błędu jest nieznaczące − co najwyżej co czwarta liczba może być silnym świadkiem pierwszości, prawdopodobieństwo, że i razy przypadkowo wybierzemy świadka jest co najwyżej 4−i.

Algorytm Rabina-Millera ma jeszcze jedno zastosowanie. Załóżmy, że r jest wykładnikiem uniwersalnym dla n, tzn. jeśli 1<a<n, NWD(a,n) = 1, to ar = 1 (mod n). Wówczas w algorytmie Rabina-Millera używamy potęgi r zamiast n−1 i na pewno nie zdarzy się przypadek bk ≠ 1. Jeśli więc liczba n jest złożona, to prawie na pewno znajdziemy jej rozkład.

Przykład wykładnika uniwersalnego, to potencjalna znajomość obu kluczy w algorytmie RSA. W algorytmie tym wybiera się dwie liczby pierwsze, p i q, definiuje się n =  p*q, następnie wybiera się dwie liczby d i e wzajemnie odwrotne (mod (p−1)*(q−1)), jednym z kluczy jest para (n,d), drugim para (n,e). Funkcje szyfrowania i odszyfrowywania wiadomości a, 1<a<n, to ae (mod n) oraz ad (mod n). Wówczas d*e−1 jest wykładnikiem uniwersalnym.

Zastosowanie algorytmu Rabina-Millera do znajdowania rozkładu jest czysto teoretyczne. Rozkład liczby n na czynniki jest potrzebny by znależć klucz prywatny (n,d) znając klucz publiczny (n,e). Gdy znane są oba klucze, szukanie rozkładu nie jest nikomu potrzebne. Jest to tylko dowód, że znajomość rozkładu jest równoważna umiejętności znajdowania klucza prywatnego. Również przypadkowe znalezienie rozkładu jest mało prawdopodobe dla liczb nie mających małych dzielników.

Zastosowanie algorytmu Rabina-Millera do testowania pierwszości jest bardzo ważne. Jest on niewiele bardziej skomplikowany niż test Fermata, a wymaga mniejszej liczby iteracji.

Uwaga: Algorytm ma zastosowanie do liczb wielkości kilkuset bitów. Dlatego też potrzebne będą specjalne narzędzia do obsługi tych liczb. W niektórych językach, np. python czy ruby są one wbudowane. Ale pisząc program w javie trzeba będzie odwołac się do biblioteki java.math.BigInteger, a w języku C - do biblioteki gmp.h.

### Zadanie:

Program o nazwie rabinmiller czyta plik wejscie.txt zawierający jeden, dwa lub trzy wiersze. W pierwszym wierszu znajduje się liczba n. Jeśli jest drugi wiersz, to zawiera on wykładnik uniwersalny, ułatwiający rozkład. Jeśli jest trzeci wiersz, to iloczyn liczb w drugim i trzecim wierszu minus jeden jest wykładnikiem uniwersalnym.

Program zapisuje w pliku wyjscie.txt jedną z trzech wiadomości: „prawdopodobnie pierwsza”, „na pewno złożona”, lub liczbę będącą dzielnikiem liczby n. Zapis „prawdopodobnie pierwsza” ma prawo się pojawić, jeśli prawdobodobieństwo, że liczba jest złożona jest mniejsza niż 2−40.

Program rabinmiller wywołany z opcją -f będzie dokonywać jedynie testu Fermata, tzn. będzie badać jedynie ostatnią potęgę potencjalnego świadka pierwszości. W szczególności, program nie będzie czytał dalszych wierszy w pliku wejściowym i nie będzie okazji do znalezienia rozkładu.

Testowy plik wejściowy będzie zawierał liczby

718548065973745507
3449
543546506135745129
program powiniem wyprodukować jeden z dwóch poniższych wyników
740876531
969862097
(ich iloczyn jest równy 718548065973745507, podczas działania programu okaże się, że 576566739470926048 jest pierwiastkiem z 1 mod 718548065973745507).
Program wywołany z opcją -f nie odkryje, że 561 (liczba Carmichaela) jest liczbą złożoną, a wywołany w pełnej wersji odkryje, że 561=33*17.
