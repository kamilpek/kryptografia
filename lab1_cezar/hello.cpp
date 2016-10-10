#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

/**
Autor: Kamil Pek 231050
Data: 10.10.2016
*/

class szyfrcezara{
public:

	szyfrcezara() {
		string sc_tekst;
		int sc_klucz;
		ifstream plain ("plain.txt");
		ifstream key ("key.txt");
		if(key.is_open()){
			key >> sc_klucz; }
		else cout << "Nie mozna odczytac klucza.";
		czyscplik();
		if(plain.is_open()){
			while(getline(plain, sc_tekst)){
				string szyfr = szyfrowanie(sc_tekst, sc_klucz);
				zapisdopliku(szyfr);
				cout << szyfr << "\n";
			}
			plain.close();
			key.close();
		}
		else cout << "Nie mozna otworzyc pliku."; }

		string szyfrowanie(string t, int k){
			int d = sizeof t;
			d--;
			for(int i=0; i<d; i++){
				int x = t[i];
				// int wynik = (x+k)%26;
				int wynik = x+5;
				t[i] = (char)wynik;
				string szyfr(t); }
			return t;
		}

		void czyscplik(){
			ofstream crypto ("crypto.txt");
			if(crypto.is_open()){
				crypto << "";
				crypto.close();	}
			else cout << "Nie mozna przeprowadzic operacji na pliku.\n";
		}

		void zapisdopliku(string s){
			ofstream crypto ("crypto.txt", ios::out|ios::app);
			if(crypto.is_open()){
				crypto << s << "\n";
				crypto.close();	}
			else cout << "Nie mozna zapisac do pliku.\n";
		}
};

int main(int argc, char * argv[]){

	szyfrcezara sc;

	// switch ((*argv)[1]) {
	// 	case "-c": 	szyfrcezara sc; break;
	// 	default:  cout << "Prosze wybrac parametr.\n";
	// }

	return 0;
}
