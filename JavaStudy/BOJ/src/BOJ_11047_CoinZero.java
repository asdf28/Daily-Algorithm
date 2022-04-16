import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
//
class BOJ_11047_CoinZero {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)) ;
        String input;
        int n, k = 0;
        int cnt = 0;
        int coin = 0;
        Stack<Integer> sCoinList = new Stack<>();

        input = br.readLine();

        n = Integer.parseInt(input.split(" ")[0]);
        k = Integer.parseInt(input.split(" ")[1]);

        for(int i = 0; i < n; i++) {
            sCoinList.add(Integer.parseInt(br.readLine()));
        }

        coin = sCoinList.pop();

        while(true) {
            cnt++;

            while(coin > k) {
                coin = sCoinList.pop();
            }

            // k에서 coin을 빼준다.
            k -= coin;

            // k가 0이 되면 종료
            if(k == 0) {
                break;
            }
        }

        bw.write(String.valueOf(cnt));

        bw.flush();
    }
}
