# Kryptografia i bezpieczeństwo systemów informatycznych
## Laboratorium 9. 15.01.2017
### Pretty Good Privacy (PGP)

PGP (pretty good privacy – cakiem niezła prywatność) jest dostępny w implementacji Gnu pod nazwą gpg.

Program gpg można używać z poziomu polecenia terminala. Pozwala on szyfrować/odszyfrowywać/podpisywać/weryfikować pliki. My jednak użyjemy go w celu obsługi poczty elektronicznej. Standardowy program pocztowy w systemie Unix/Ubuntu, czyli Evolution, już jest zintegrowany z programem GPG. W przypadku programu Thunderbird/Mozilla taka integracja wymaga przygotowania -- trzeba użyć rozszerzenia. Oczywiście zawsze można pliki przygotować poza programem pocztowym i wysyłać używając dowolnej metody obsługi poczty.

W PGP występuje kilka scenariuszy użycia.

    generowanie własnych kluczy,

    podpisywanie plików, wymaga dostępu do własnego klucza prywatnego,

    odszyfrowywanie plików, przedtem trzeba udostępnić własny klucz publiczny innym, by mogli szyfrować,

    instalacja cudzych kluczy publicznych, niezbędnych do szyfrowania i weryfikacji podpisu,

    szyfrowanie/weryfikacja podpisu, wymaga znajomości cudzego klucza publicznego.

Wszystkie operacje PGP można wykonać używając terminala tekstowego. I tak:

    generowanie kluczy: gpg --gen-key,

    podpisywanie pliku: gpg -s [nazwa pliku],
    wersja produkująca podpis odrębnie od pliku (przydatna szczególnie przy podpisywaniu plików binarnych, których struktura nie powinna ulec zmianie): gpg -s -b [nazwa pliku],

    eksportowanie własnego klucza: gpg --export > [nazwa pliku],
    pliki generowane przez GPG są domyślnie w postaci binarnej. Jeśli mają być w postaci tekstowej, trzeba użyć opcji -a,

    odszyfrowywanie pliku: gpg [nazwa pliku],

    instalacja cudzych kluczy publicznych: gpg --import [nazwa pliku],

    szyfrowanie: gpg -e [nazwa pliku],

    weryfikacja podpisu: gpg [nazwa pliku],

    sprawdzenie posiadanych kluczy: gpg --list-keys,

    usunięcie klucza prywatnego: gpg --delete-secret-key name.

### Zadania:

    Wygeneruj dla siebie parę kluczy, klucz powinien zawierać imię, nazwisko, email oraz komentarz "laboratorium z kryptografii". Powinien być ważny najwyżej kilka dni, może tylko ten jeden dzień (UWAGA: klucz powinien być chroniony hasłem, hasło powinno być pamiętane przynajmniej do końca dzisiejszych zajęć). Swój klucz publiczny w wersji tekstowej (tzn. nazwa w formacie 0x...asc) umieść jako rozwiązanie zadania.

    Przygotuj plik dane.txt zawierający imię, nazwisko, numer indeksu i bieżącą datę. Umieść jako rozwiązanie zadania plik tekstowy o nazwie dane.txt.asc zawierający podpisaną przez siebie powyższą wiadomość.

    Zainstaluj klucze publiczne dostępne pod adresem [0x4DB19f11.asc](https://github.com/kamilpek/kryptografia/blob/master/lab9_pgp/0x4DB19f11.asc) oraz [0x484452D4.asc](https://github.com/kamilpek/kryptografia/blob/master/lab9_pgp/0x484452D4.asc). Przygotuj plik zawierający odpowiedź na pytanie do kogo należą powyższe klucze i do kiedy są ważne. Zaszyfruj ten plik odpowiednim kluczem publicznym (tylko jeden jest sensowny) i umieść jako rozwiązanie zadania. Nazwą pliku będzie crypto.txt.asc.
