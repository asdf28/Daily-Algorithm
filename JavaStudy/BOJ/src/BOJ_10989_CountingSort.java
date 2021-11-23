import java.io.*;

public class BOJ_10989_CountingSort {
    public static void main(String[] args){
        try {
            BufferedReader  Reader = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter  Writer = new BufferedWriter(new OutputStreamWriter(System.out));
            int[]           arr = new int[10001];
            int             N;
            int             i;
            int             j;

            N = Integer.parseInt(Reader.readLine());

            for(i = 0; i < N; i++) {
                arr[Integer.parseInt(Reader.readLine())] += 1;
            }

            for(i = 1; i <=10000; i++){
                if(arr[i] == 0) {
                    continue;
                }
                for(j = 0; j < arr[i]; j++) {
                    System.out.println(i);
                }
            }

        }catch (IOException e){
            e.printStackTrace();
        }

    }
}
