#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

/**
Autor: Kamil Pek 231050
Data: 16.10.2016
*/

class pliki{
public:

	void zapisz(string s, int tryb){				// ios::app -> dopisywanie do pliku
		ofstream crypto ("crypto.txt", ios::app);
		ofstream decrypt ("decrypt.txt", ios::app);
		if(tryb == 1){
			if(crypto.is_open()){
				crypto << s << "\n";
				crypto.close();	}
			else cout << "Nie mozna zapisac do pliku.\n";	}
		else if(tryb == 2){
			if(decrypt.is_open()){
				// cout << "elo";
				decrypt << s << "\n";
				decrypt.close(); }
			else cout << "Nie mozna zapisac do pliku.\n";	}
	}

	int odczytklucza(){
		int klucz;
		ifstream key("key.txt");
		if(key.is_open()){
			key >> klucz;
			if(klucz >= -26 && klucz <= 26) return klucz;
			else cout << "Nieprawidlowy klucz w pliku key.txt\n";
			key.close(); }
		else cout << "Nie mozna odczytac pliku key.txt\n";
		return klucz;
	}

	void czyscplik(){
		ofstream crypto ("crypto.txt");
		if(crypto.is_open()){
			crypto << "";
			crypto.close();	}
		else cout << "Nie mozna przeprowadzic operacji na pliku.\n";
	}

	int wielkosc(char znak){
		if(znak >= 'a' && znak <= 'z') return 0;
		if(znak >= 'A' && znak <= 'Z') return 1;
		else return 2; // pozostale znaki
	}

};

class szyfrcezara{
public:
	pliki obsluga;

	szyfrcezara(int tryb) {
		int sc_klucz = obsluga.odczytklucza();
		string sc_tekst;
		string sc_zaszyfr;
		if(tryb == 1){
			obsluga.czyscplik();
			ifstream plain("plain.txt");
			if(plain.is_open()){
				while(getline(plain, sc_tekst)){
					string szyfr = szyfrowanie(sc_tekst, sc_klucz);
					obsluga.zapisz(szyfr, 1); }
				plain.close(); } }
		if(tryb == 2){
			ifstream crypto("crypto.txt");
			if(crypto.is_open()){
				while(getline(crypto, sc_zaszyfr)){
					string tresc = deszyfrowanie(sc_zaszyfr, sc_klucz);
					obsluga.zapisz(tresc, 2); }
				crypto.close(); }	}
}

		string szyfrowanie(string &t, int k){
			char a, z;
			int d = t.size();
			for(int i = 0; i < d; i++){
				int w = obsluga.wielkosc(t[i]);
				if(w == 0) a = 'a', z = 'z';
				else a = 'A', z = 'Z';
				if(k >= 0){
					if(t[i] + k <= z) t[i] += k;
					else t[i] = t[i] + k - 26; }
				else {
					if(t[i] + k >= a) t[i] += k;
					else t[i] = t[i] + k + 26; } }
			return t;
		}

		string deszyfrowanie(string &t, int k){
			char a, z;
			int d = t.size();
			for(int i = 0; i < d; i++){
				int w = obsluga.wielkosc(t[i]);
				if(w == 0) a = 'a', z = 'z';
				else a = 'A', z = 'Z';
				if(k >= 0){
					if(t[i] - k <= z) t[i] -= k;
					else t[i] = t[i] - k + 26; }
				else {
					if(t[i] - k >= a) t[i] -= k;
					else t[i] = t[i] - k - 26; } }
				return t;
			}
};

int main(int argc, char * argv[]){

	if ( !strcmp(argv[1], "-c") && !strcmp(argv[2], "-e") ) szyfrcezara sc(1);
	else if ( !strcmp(argv[1], "-c") && !strcmp(argv[2], "-d") ) szyfrcezara sc(2);
	else if ( !strcmp(argv[1], "-c") && !strcmp(argv[2], "-j") ) szyfrcezara sc(3);
	else if ( !strcmp(argv[1], "-c") && !strcmp(argv[2], "-k") ) szyfrcezara sc(4);

	if ( !strcmp(argv[1], "-a") && !strcmp(argv[2], "-e") ) cout << "Wybrano Szyfr afiniczny.\nSzyfrowanie.\n";
	else if ( !strcmp(argv[1], "-a") && !strcmp(argv[2], "-d")) cout << "Wybrano Szyfr afiniczny.\nOdszyfrowywanie.\n";
	else if ( !strcmp(argv[1], "-a") && !strcmp(argv[2], "-j")) cout << "Wybrano Szyfr afiniczny.\nKryptoanaliza z tekstem jawnym.\n";
	else if ( !strcmp(argv[1], "-a") && !strcmp(argv[2], "-k")) cout << "Wybrano Szyfr afiniczny.\nKryptoanaliza wyłącznie w oparciu o kryptogram.\n";

	return 0;
}
