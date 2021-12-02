import java.io.*;
import java.util.LinkedList;
import java.util.Stack;

public class BOJ_2108_Statistics {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)) ;
        int[] CountArr;
        int[] ResArr;
        int[] OrgArr;
        int Accumulator = 0;
        int N;
        int Input;
        double ArithArg = 0;
        int[] Mode =  new int[2];
        int ModeFreq = -1;

        N = Integer.parseInt(br.readLine());

        OrgArr = new int[N];
        ResArr = new int[N];
        CountArr = new int[8001];

        for(int i = 0; i < N; i++) {
            Input = Integer.parseInt(br.readLine());

            OrgArr[i] = Input;
            ArithArg += Input;
            CountArr[Input + 4000]++;
        }

        for(int i = 0; i <= 8000; i++){
            if(CountArr[i] == 0) {
                continue;
            }

            if(ModeFreq < CountArr[i]) {
                ModeFreq = CountArr[i];
                Mode[0] = i-4000;
                Mode[1] = 9999;
            }

            else if(ModeFreq == CountArr[i]) {
                if(Mode[0] > i-4000) {
                    Mode[1] = Mode[0];
                    Mode[0] = i-4000;
                }
                else if(Mode[1] > i-4000 && Mode[0] < i-4000) {
                    Mode[1] = i-4000;
                }
            }
            Accumulator += CountArr[i];
            CountArr[i] = Accumulator;
        }

        for(int i = 0; i < N; i++) {
            ResArr[CountArr[OrgArr[i]+4000]-1] = OrgArr[i];
            CountArr[OrgArr[i]+4000] -= 1;
        }

        if(Mode[1] == 9999){
            Mode[1] = Mode[0];
        }

        if(ArithArg < 0) {
            ArithArg *= -1;
            ArithArg /= N;
            ArithArg = Math.round(ArithArg);
            ArithArg *= -1;
        }
        else {
            ArithArg /= N;
        }
        bw.write(Math.round(ArithArg) + "\n");
        bw.write(ResArr[N/2] + "\n");
        bw.write(Mode[1] + "\n");
        bw.write(ResArr[N-1] - ResArr[0]+ "\n");

        bw.flush();

    }
}
