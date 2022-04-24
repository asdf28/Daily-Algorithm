import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_13305_OilStation {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)) ;
        StringTokenizer strTok;
        int[]                    distance, city;
        int                      minOilPrice = Integer.MAX_VALUE;
        int                      curOilPrice;
        long                     totalOilPrice = 0;
        int                      n;

        n = Integer.parseInt(br.readLine());

        distance = new int[n-1];
        city = new int[n];

        strTok = new StringTokenizer(br.readLine(), " ");

        for(int i = 0; i < n-1; i++) {
            distance[i] = Integer.parseInt(strTok.nextToken());
        }

        strTok = new StringTokenizer(br.readLine(), " ");

        for(int i = 0; i < n; i++) {
            city[i] = Integer.parseInt(strTok.nextToken());
        }

        for(int i = 0; i < n-1; i++) {
            curOilPrice = city[i];

            if (curOilPrice < minOilPrice) {
                minOilPrice = curOilPrice;
            }

            totalOilPrice += (long) minOilPrice * distance[i];
        }

        bw.write(String.valueOf(totalOilPrice));
        bw.flush();
    }
}
