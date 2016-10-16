#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

/**
Autor: Kamil Pek 231050
Data: 16.10.2016
*/

class szyfrcezara{
public:

	szyfrcezara() {
		string sc_tekst;
		int sc_klucz;
		ifstream plain ("plain.txt");
		ifstream key ("key.txt");
		if(key.is_open()){
			key >> sc_klucz;
			key.close(); }
		else cout << "Nie mozna odczytac klucza.";
		czyscplik();
		if(plain.is_open()){
			while(getline(plain, sc_tekst)){
				string szyfr = szyfrowanie(sc_tekst, sc_klucz);
				zapisdopliku(szyfr); }
			plain.close(); }
		else cout << "Nie mozna otworzyc pliku."; }

		string szyfrowanie(string &t, int k){
			char a, z;
			int d = t.size();
			for(int i = 0; i < d; i++){
				int w = wielkosc(t[i]);
				if (w == 0) a = 'a', z = 'z';
				else a = 'A', z = 'Z';
				if(k >= 0){
					if (t[i] + k <= z) t[i] += k;
					else t[i] = t[i] + k - 26; }
				else {
					if (t[i] + k >= a) t[i] += k;
					else t[i] = t[i] + k + 26; } }
			return t;
		}

		void czyscplik(){
			ofstream crypto ("crypto.txt");
			if(crypto.is_open()){
				crypto << "";
				crypto.close();	}
			else cout << "Nie mozna przeprowadzic operacji na pliku.\n";
		}

		void zapisdopliku(string s){     // ios::app - dopisywanie do pliku
			ofstream crypto ("crypto.txt", ios::app);
			if(crypto.is_open()){
				crypto << s << "\n";
				crypto.close();	}
			else cout << "Nie mozna zapisac do pliku.\n";
		}

		int wielkosc(char znak){
			if(znak >= 'a' && znak <= 'z') return 0;
			if(znak >= 'A' && znak <= 'Z') return 1;
			else return 2; // pozostale znaki
		}
};

int main(int argc, char * argv[]){

	if ( !strcmp(argv[1], "-c")) cout << "Wybrano Szyfr Cezara.\n";
	else if ( !strcmp(argv[1], "-a")) cout << "Wybrano Szyfr afiniczny.\n";

	if ( !strcmp(argv[2], "-e")) cout << "Szyfrowanie.\n";
	else if ( !strcmp(argv[2], "-d")) cout << "Odszyfrowywanie.\n";
	else if ( !strcmp(argv[2], "-j")) cout << "Kryptoanaliza z tekstem jawnym.\n";
	else if ( !strcmp(argv[2], "-k")) cout << "Kryptoanaliza wyłącznie w oparciu o kryptogram.\n";
	else cout << "Prosze podac parametr.\n";

	return 0;
}
