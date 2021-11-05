
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class BOJ_2751_Sorting2 {

    public static void main (String[] args) {
        try {
            BufferedReader Reader = null;
            BufferedWriter Writer = null;
            ArrayList<Integer> arr = null;
            int N = 0;


            Reader = new BufferedReader(new InputStreamReader(System.in));
            Writer = new BufferedWriter(new OutputStreamWriter(System.out));

            arr = new ArrayList<Integer>();

            N = Integer.parseInt(Reader.readLine());

            for (int i = 0; i < N; i++) {
                arr.add(Integer.parseInt(Reader.readLine()));
            }

            Collections.sort(arr);

            for (int i : arr) {
                Writer.write(String.valueOf(i));
                Writer.newLine();
            }
            Writer.flush();
        } catch(IOException e){
            e.printStackTrace();
        }
    }

}
