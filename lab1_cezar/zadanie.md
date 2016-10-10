#Kryptografia i bezpieczeństwo systemów informatycznych
## Laboratorium 1. 09.10.2016
W oryginalnej definicji szyfrów podstawieniowych zakładano, że w tekście jawnym nie ma spacji ani znaków przestankowych, nie rozróżniano też małych i wielkich liter. Zmniejszało to bardzo czytelność tekstów, od tych założeń odchodzimy. Pewnym problemem jest też obecność polskich liter, można tekst jawny poddać wstępnemu przetwarzaniu i założyć, że polskie litery zostały usunięte, można też przyjąć, że alfabet jest dłuższy niż w języku angielskim i zmodyfikować odpowiednio algorytmy.

Zakładamy, że litery zakodowane są za pomocą liczb 0..25, spacje, znaki przestankowe i cyfry pozostaną nienaruszone, niezmieniona też będzie wielkość liter (tzn. małe litery będziemy szyfrować za pomocą małych liter, a wielkie wielkimi literami. Zmniejsza to oczywiście radykalnie bezpieczeństwo szyfru, ale jest ono i tak bliskie zeru.

W poniższym x oznacza tekst jawny, y kryptogram, k klucz, E funkcję szyfrującą, a D funkcję odszyfrowywania.

szyfr Cezara: E(k,x)=x+k (mod 26), D(k,y)=y-k (mod 26), klucz k jest liczbą z zakresu 1..25.

szyfr afiniczny: E(a,b,x)=a*x+b (mod 26), D(a,b,y)=a'*(y-b) (mod 26) gdzie klucz jest parą liczb (a,b) takich, że NWD(a,26)=1 oraz a*a'=1 (mod 26).

###Zadanie:

Zaprogramować szyfrowanie i odszyfrowywanie wiadomości przy użyciu szyfru Cezara i szyfru afinicznego.

Program o nazwie cezar powinien umożliwiać wywołanie z linijki rozkazowej z następującymi opcjami:

-c (szyfr Cezara),
-a (szyfr afiniczny),
-e (szyfrowanie),
-d (odszyfrowywanie),
-j (kryptoanaliza z tekstem jawnym),
-k (kryptoanaliza wyłącznie w oparciu o kryptogram)

Program będzie czytał dane z pewnych plików i zapisywał na inne, nazwy tych plików są z góry ustalone:

plain.txt: plik z tekstem jawnym,
crypto.txt: plik z tekstem zaszyfrowanym,
decrypt.txt: plik z tekstem odszyfrowanym,
key.txt: plik zawierający klucz,
extra.txt: plik zawierający pomocniczy tekst jawny w przypadku kryptoanalizy z tekstem jawnym i zaszyfrowanym.

Program szyfrujący czyta tekst jawny i klucz i zapisuje tekst zaszyfrowany. Jeśli klucz jest nieprawidłowy, zgłasza jedynie błąd.

Program odszyfrowujący czyta tekst zaszyfrowany i klucz i zapisuje tekst jawny. Jeśli klucz jest nieprawidłowy, zgłasza błąd. Dla szyfru afinicznego częścią zadania jest znalezienie odwrotności dla liczby a podanej jako część klucza – nie można zakładać, że program odszyfrowujący otrzymuje tę odwrotność.

Program łamiący szyfr z pomocą tekstu jawnego czyta tekst zaszyfrowany, tekst pomocniczy i zapisuje obliczony klucz i odszyfrowany tekst. Jeśli niemożliwe jest obliczenie klucza, zgłasza sygnał błędu.

Program łamiący szyfr bez pomocy tekstu jawnego czyta jedynie tekst zaszyfrowany i zapisuje jako tekst jawny wszystkie możliwe kandydatury (25 dla szyfru Cezara, 312 dla szyfru afinicznego).
