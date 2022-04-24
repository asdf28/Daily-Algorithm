import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_11399_ATM {
    public void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)) ;
        ArrayList<Integer> line;
        String                   input;
        int                      n;
        int                      currentWaitTime = 0, totalWaitTime = 0;

        n = Integer.parseInt(br.readLine());
        line = new ArrayList<>(n);

        input = br.readLine();

        for(int i = 0; i < n; i++) {
            line.add(Integer.parseInt(input.split(" ")[i]));
        }

        Collections.sort(line);

        for(int i = 0; i < n; i++) {
            currentWaitTime += line.get(i);
            totalWaitTime += currentWaitTime;
        }

        bw.write(String.valueOf(totalWaitTime));
        bw.flush();
    }
}
