import java.io.*;

public class xor{

  public void kryptoanaliza(){
    File crypto = new File("crypto.txt");
    File decrypt = new File("decrypt.txt");
    try {
      try {
        try {
          Reader reader = new InputStreamReader(new FileInputStream(crypto),"US-ASCII");
          BufferedReader fin = new BufferedReader(reader);
          Writer writer = new OutputStreamWriter(new FileOutputStream(decrypt), "US-ASCII");
          BufferedWriter fout = new BufferedWriter(writer);
          int z = 20, y = 0;

          String tekst = fin.readLine();
          int dlugosctekstu = tekst.length();
          byte[][] tab = new byte[z][dlugosctekstu];
          while(tekst!=null){
            tab[y] = tekst.getBytes("US-ASCII");
            y += 1;
            tekst = fin.readLine();
          }
          fin.close();
          byte[] bytes = new byte[dlugosctekstu];
          int[] bajtyhasla = new int[dlugosctekstu];
          for(int x = 0; x <= 19; x++){
            for(y = 0; y <= dlugosctekstu-1; y++ ){
              if(tab[x][y] < 58){
                bytes[y] = 32;
                bajtyhasla[y] = tab[x][y] - bytes[y];
              }
            }
          }
          int w =0;
          char[] znak = new char[dlugosctekstu];
          StringBuilder sB = new StringBuilder(znak[w]);
          String wyjscie = "";
          for(int x = 0; x <= 19; x++){
            for(y = 0; y <= dlugosctekstu-1; y++ ){
                tab[x][y] -= bajtyhasla[y];
                if (tab[x][y] < 97 && tab[x][y] > 33) { tab[x][y] += 25; }
                znak[y] = (char)tab[x][y];
                sB.append(znak[y]);
              }
              sB.append("\n");
            }
            wyjscie = sB.toString();
            fout.write(wyjscie);
            fout.close();
        } catch (UnsupportedEncodingException e) {}
      } catch (FileNotFoundException e) {}
    } catch (IOException e) {}
  }

  public void szyfruj(byte[] klucz){
   File plain = new File("plain.txt");
   File crypto = new File("crypto.txt");
   String tekst="", all = "";
   StringBuilder sB = new StringBuilder(tekst);
   int wynik = 0;
   try {
     try {
       try {
         Reader reader = new InputStreamReader(new FileInputStream(plain),"US-ASCII");
         BufferedReader fin = new BufferedReader(reader);
         Writer writer = new OutputStreamWriter(new FileOutputStream(crypto), "US-ASCII");
         BufferedWriter fout = new BufferedWriter(writer);
         tekst = fin.readLine();
         while (tekst!=null) {
           sB.append(tekst);
           sB.append("\n");
           tekst = fin.readLine();
         }
         all = sB.toString();
         byte[] bytes = all.getBytes("US-ASCII");
         int z = 0, i= 0;
         char[] znak = new char[bytes.length];
         StringBuilder record = new StringBuilder(znak[i]);
         for (i=0;i<=bytes.length-1;i++ ) {
           if(z>=klucz.length-1){ z = 0; }
           wynik = bytes[i] + klucz[z];
           z += 1;
           if(wynik>122){ wynik-=25; }
           if(bytes[i]==10){ wynik = 10; z = 0; }
           znak[i] = (char)wynik;
           record.append(znak[i]);
         }
         all = record.toString();
         fout.write(all);
         fout.close();
         fin.close();
       } catch (UnsupportedEncodingException e) {}
     } catch (FileNotFoundException e) {}
   } catch (IOException e) {}
 }

  public byte[] kluczdoascii(){
   String klucz = new String("");
   File fkey = new File("key.txt");
   try {
   try {
     Reader reader2 = new InputStreamReader(new FileInputStream(fkey),"ASCII");
     BufferedReader key = new BufferedReader(reader2);
   try {
     klucz = key.readLine();
     byte[] bytes = klucz.getBytes("US-ASCII");
     for(int i=0; i<=klucz.length()-1; i++){
       bytes[i] -= 97;
     }
     return bytes;
   } catch (UnsupportedEncodingException e) {}
   } catch (FileNotFoundException e) { System.out.println("Brak pliku z kluczem");  }
   } catch (IOException e) { System.out.println("Problem we/wy"); }
   return null;
 }

  public void przygotuj(){
    File orig = new File("orig.txt");
    File plain = new File("plain.txt");
    String tekst = "", all = "";
    StringBuilder sB = new StringBuilder(all);
    try {
      try {
        try {
          Reader reader = new InputStreamReader(new FileInputStream(orig),"ASCII");
          BufferedReader fin = new BufferedReader(reader);
          Writer writer = new OutputStreamWriter(new FileOutputStream(plain), "UTF-8");
          BufferedWriter fout = new BufferedWriter(writer);
          String tekscik = "";
          tekst = fin.readLine();
          // while(tekst!=null){
          //   tekst = tekst.replaceAll("[-,.!?:;'-0123456789]", "");
          //   tekst = tekst.toLowerCase();
          //   for (String retval: tekst.split("(?<=\\G.{35})")){
          //     sB.append(retval);
          //     sB.append("\n");
          //   }
          //   sB.append("\n");
          //   tekst = fin.readLine();
          // }
          while(tekst!=null){
            tekst = tekst.replaceAll("[,.!?:;'-0123456789]", "");
            tekst = tekst.toLowerCase();
            tekscik = tekst.substring(0, 35);
            sB.append(tekscik);
            sB.append("\n");
            tekst = fin.readLine();
          }
          all = sB.toString();
          fout.write(all);
          fin.close();
          fout.close();
        } catch (UnsupportedEncodingException e) {}
      } catch (FileNotFoundException e) {}
    } catch (IOException e) {}
  }

  public static void main(String[] args) {
    String[] x = args;
    byte[] klucz;
    xor start = new xor();
    switch (x[0]) {

      case "-p":
      start.przygotuj();
      break;

      case "-e":
      klucz = start.kluczdoascii();
      start.szyfruj(klucz);
      break;

      case "-k":
      start.kryptoanaliza();
      //kryptoanaliza
    }
  }
}
