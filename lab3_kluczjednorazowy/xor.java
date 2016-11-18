import java.io.*;

public class xor{

  public void prepare(){
    File orig = new File("orig.txt");
    File plain = new File("plain.txt");
    String tresc = "", all = "";
    StringBuilder sB = new StringBuilder(all);
    try {
      try {
        try {
          Reader reader = new InputStreamReader(new FileInputStream(orig),"ASCII");
          BufferedReader fin = new BufferedReader(reader);
          Writer writer = new OutputStreamWriter(new FileOutputStream(plain), "UTF-8");
          BufferedWriter fout = new BufferedWriter(writer);
          String tekscik = "";
          tresc = fin.readLine();
          while(tresc!=null){
            tresc = tresc.replaceAll("[,.!?:;'-0123456789]", "");
            tresc = tresc.toLowerCase();
            tekscik = tresc.substring(0, 35);
            sB.append(tekscik);
            sB.append("\n");
            tresc = fin.readLine();
          }
          all = sB.toString();
          fout.write(all);
          fin.close();
          fout.close();
        } catch (UnsupportedEncodingException e) {}
      } catch (FileNotFoundException e) {}
    } catch (IOException e) {}
  }

  public void cryptanalysis(){
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

          String tresc = fin.readLine();
          int lentresc = tresc.length();
          byte[][] arr = new byte[z][lentresc];
          while(tresc!=null){
            arr[y] = tresc.getBytes("US-ASCII");
            y += 1;
            tresc = fin.readLine();
          }
          fin.close();
          byte[] bytes = new byte[lentresc];
          int[] bajtyhasla = new int[lentresc];
          for(int x = 0; x <= 19; x++){
            for(y = 0; y <= lentresc-1; y++ ){
              if(arr[x][y] < 58){
                bytes[y] = 32;
                bajtyhasla[y] = arr[x][y] - bytes[y];
              }
            }
          }
          int w =0;
          char[] chr = new char[lentresc];
          StringBuilder sB = new StringBuilder(chr[w]);
          String out = "";
          for(int x = 0; x <= 19; x++){
            for(y = 0; y <= lentresc-1; y++ ){
                arr[x][y] -= bajtyhasla[y];
                if (arr[x][y] < 97 && arr[x][y] > 33) { arr[x][y] += 25; }
                chr[y] = (char)arr[x][y];
                sB.append(chr[y]);
              }
              sB.append("\n");
            }
            out = sB.toString();
            fout.write(out);
            fout.close();
        } catch (UnsupportedEncodingException e) {}
      } catch (FileNotFoundException e) {}
    } catch (IOException e) {}
  }

  public byte[] asciikey(){
   String akey = new String("");
   File fkey = new File("key.txt");
   try {
   try {
     Reader reader2 = new InputStreamReader(new FileInputStream(fkey),"ASCII");
     BufferedReader key = new BufferedReader(reader2);
   try {
     akey = key.readLine();
     byte[] bytes = akey.getBytes("US-ASCII");
     for(int i=0; i<=akey.length()-1; i++){
       bytes[i] -= 97;
     }
     return bytes;
   } catch (UnsupportedEncodingException e) {}
   } catch (FileNotFoundException e) { System.out.println("Brak pliku z kluczem");  }
   } catch (IOException e) { System.out.println("Problem we/wy"); }
   return null;
 }

  public void encrypt(){
   File plain = new File("plain.txt");
   File crypto = new File("crypto.txt");
   byte[] key;
   key = this.asciikey();
   String tresc="", all = "";
   StringBuilder sB = new StringBuilder(tresc);
   int result = 0;
   try {
     try {
       try {
         Reader reader = new InputStreamReader(new FileInputStream(plain),"US-ASCII");
         BufferedReader fin = new BufferedReader(reader);
         Writer writer = new OutputStreamWriter(new FileOutputStream(crypto), "US-ASCII");
         BufferedWriter fout = new BufferedWriter(writer);
         tresc = fin.readLine();
         while (tresc!=null) {
           sB.append(tresc);
           sB.append("\n");
           tresc = fin.readLine();
         }
         all = sB.toString();
         byte[] bytes = all.getBytes("US-ASCII");
         int z = 0, i= 0;
         char[] chr = new char[bytes.length];
         StringBuilder record = new StringBuilder(chr[i]);
         for (i=0;i<=bytes.length-1;i++ ) {
           if(z>=key.length-1){ z = 0; }
           result = bytes[i] + key[z];
           z += 1;
           if(result>122){ result-=25; }
           if(bytes[i]==10){ result = 10; z = 0; }
           chr[i] = (char)result;
           record.append(chr[i]);
         }
         all = record.toString();
         fout.write(all);
         fout.close();
         fin.close();
       } catch (UnsupportedEncodingException e) {}
     } catch (FileNotFoundException e) {}
   } catch (IOException e) {}
 }

  public static void main(String[] args) {
    String[] x = args;
    byte[] key;
    xor start = new xor();
    switch (x[0]) {

      case "-p": start.prepare(); break;

      case "-e":
      // key = start.asciikey();
      start.encrypt();
      break;

      case "-k": start.cryptanalysis();
    }
  }
}
