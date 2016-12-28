# Kryptografia i bezpieczeństwo systemów informatycznych
## Laboratorium 7. 18.12.2016

System ten opiera się o trudność problemu Diffie-Hellmana, wersja bardziej złożona jest podstawą amerykańskiego standardu podpisu cyfrowego DSA. Przygotowanie kluczy wymaga znalezienie liczby p, jeśli nie pseudopierwszej, to przynajmniej takiej, że p−1 ma duży dzielnik pierwszy. W zadaniu poniższym dla uproszczenia nie będziemy się tym zajmować.

Następnym problemem jest znalezienie generatora. g jest generatorem Zp* = {1,2,...,p−1} jeśli kolejne potęgi g mod p wyczerpują cały zbiór reszt. Generatorów jest dość dużo (dokładniej, ich liczba jest równa liczbie Eulera φ(p−1)). Na ogół wystarczy przejrzeć kilka małych liczb by znaleźć generator. Na pewno gp−1 = 1 (mod p). Liczba g nie jest generatorem, jeśli już mniejsza potęga jest równa 1 (bo wówczas niektóre wartości nie wystąpią wcale). Jeśli mniejsza potęga jest równa 1, to musi ona być dzielnikiem p−1, wystarczy więc skupić się na obliczeniu niektórych tylko potęg. W programie znajdowania generatora trzeba będzie znaleźć dzielniki γ liczby p−1 mniejsze niż ustalona liczba, np. 1000 (w realnym programie należałoby rozważać znacznie większe dzielniki), a następnie testować czy g(p−1)/γ = 1 (mod p). Jeśli tak, to g na pewno nie jest generatorem i trzeba testować kolejnego kandydata. W przeciwnym przypadku, z dużym prawdopodobieństwem można założyć, że g generatorem jest.

**Kryptosystem ElGamala**: dane są liczba pierwsza p oraz generator g grupy Zp* = {1,2,...,p−1}. Mogą być one ustalone jeden raz dla większej liczby uczestników. Kluczem prywatnym Bolka jest dowolna liczba b, a kluczem publicznym potęga β=gb (mod p). Nie można obliczyć wykładnika ze znajomości potęgi, ale oczywiście zależność odwrotna nie zachodzi. Tak więc kluczy tych nie można zamienić miejscami. Algorytmy szyfrowania i podpisu cyfrowego muszą być różne.

**Szyfrowanie**: Alicja chce wysłać do Bolka wiadomość m<p. Losuje liczbę k. Szyfrogramem tej wiadomości jest para <gk, m*βk>, (mod p).

Bolek najpierw oblicza czynnik zaciemniający βk = (gb)k = (gk)b (mod p). Potem wykonuje dzielenie by obliczyć m.

**Podpis**: Bolek chce podpisać wiadomość m<p. Losuje liczbę k względnie pierwszą z p−1. Podpis pod tą wiadomością składa się z dwu części: r=gk (mod p) oraz x = (m−b*r)*k−1 (mod p−1). Sama wiadomość m też musi być przekazana.

Alicja weryfikuje podpis sprawdzając równość (mod p) dwu wielkości: gm oraz rx*βr.

### Zadanie:

Program o nazwie elgamal wywołany z opcją
* -g generuje liczbę pierwszą p, generator g i zapisuje je jako kolejne wiersze w pliku elgamal.txt.
* -k czyta z powyższego pliku i generuje parę kluczy zapisanych w plikach private.txt oraz public.txt. Każdy klucz składa się z dwu wierszy skopiowanych z powyższego pliku oraz trzeciego wiersza zawierającego odpowiednio wykładnik lub potęgę.
* -e odczytuje klucz publiczny, następnie odczytuje wiadomość z pliku plain.txt i zapisuje zaszyfrowaną wiadomość w pliku crypto.txt. Jeśli warunek m<p nie jest spełniony, sygnalizuje błąd.
* -d odczytuje klucz prywatny i kryptogram, a odszyfrowaną wiadomość zapisuje w pliku decrypt.txt.
* -s odczytuje klucz prywatny, następnie odczytuje wiadomość z pliku message.txt i produkuje podpis, czyli dwa wiersze zapisane do pliku signature.txt.
* -v odczytuje klucz publiczny, wiadomość z pliku message.txt oraz podpis z pliku signature.txt i weryfikuje ten podpis. Wynik weryfikacji jest wyświetlany na ekranie ale również zapisywany w pliku verify.txt.
Pliki plain.txt oraz message.txt w zasadzie mogą być identyczne.
W przypadku, gdy ktoś nie posiada możliwości znalezienia dużej liczby pierwszej i generatora, może użyć poniższych danych:

1665997633093155705263923663680487185948531888850484859473375695734301776192932338784530163
 170057347237941209366519667629336535698946063913573988287540019819022183488419112350737049
dalsze działanie programu wymaga jedynie potęgowania i innych działań arytmetyki modularnej.
Sprawdzenie poprawności programu będzie m.in. zawierało sprawdzenie identyczności plików plain.txt oraz decrypt.txt oraz sprawdzenie poprawności weryfikowania podpisu poprawnego (tzn. signature.txt powstał w opisany wyżej sposób) i niepoprawnego w przeciwnym przypadku.
