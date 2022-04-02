import java.io.*;

public class BOJ_2447_CountingStar {
    static String[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)) ;

        int N = Integer.parseInt(br.readLine());

        arr = new String[N][N];

        for(int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = " ";
            }
        }

        recursion(0,0, N);

        for(int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                bw.write(arr[i][j]);
            }
            bw.newLine();
        }
        bw.flush();
    }

    static void recursion(int x, int y, int depth) {
        if(depth == 1) {
            arr[x][y] = "*";
            return;
        }

        int nextDepth = depth/3;

        recursion(x, y, nextDepth); // 1. 좌상단
        recursion(x + nextDepth, y, nextDepth); // 상단
        recursion(x + (2 * nextDepth), y, nextDepth); // 우상단
        recursion(x, y + nextDepth, nextDepth); // 좌
        //recursion(); // 가운데!!!
        recursion(x + (2 * nextDepth), y + nextDepth, nextDepth); // 우
        recursion(x, y + (2 * nextDepth), nextDepth); // 좌하단
        recursion(x + nextDepth, y + (2 * nextDepth), nextDepth); // 하
        recursion(x + (2 * nextDepth), y + (2 * nextDepth), nextDepth); // 우하단
    }

}
