import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class TICT_3_3_CardGame {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = null;
        ArrayList<ArrayList<Integer>> cards;
        ArrayList<Integer> tmpList;
        int n, m;
        int ans = 0;

        input = br.readLine();

        n = Integer.parseInt(input.split(" ")[0]);
        m = Integer.parseInt(input.split(" ")[1]);

        cards = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            input = br.readLine();

            tmpList = new ArrayList<>();
            for(int j = 0; j < m; j++){
                tmpList.add(Integer.parseInt(input.split(" ")[j]));
            }

            Collections.sort(tmpList);

            cards.add(tmpList);
        }

        for(int i = 0; i < n; i++) {
            if(ans < cards.get(i).get(0)) {
                ans = cards.get(i).get(0);
            }
        }

        bw.write(String.valueOf(ans));
        bw.flush();
    }
}
