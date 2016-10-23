#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

/**
Kamil Pek 231050
23.10.2016
*/

class przygotuj{
public:
  przygotuj(){
    cout << "Przygotowywanie tekstu do szyfrowania\n";
  }
};

class vigenere{
public:
  vigenere(int tryb){
    if(tryb == 1){
      cout << "Szyfrowanie szyfrem Vigenere\n"; }
    if(tryb == 2){
      cout << "Deszyfrowanie szyfrem Vigenere\n"; }
    if(tryb == 3){
      cout << "Kryptoanaliza szyfru Vigenere\n"; }
  }
};

int main(int argc, char * argv[]){
  if(!strcmp(argv[1], "-p")) przygotuj pp();
  else if(!strcmp(argv[1], "-e")) vigenere vg(1);
  else if(!strcmp(argv[1], "-d")) vigenere vg(2);
  else if(!strcmp(argv[1], "-k")) vigenere vg(3);
}
