import java.io.*;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;

public class BOJ_18870_PositionCompression {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n;
        int num;
        String input;
        int seq;
        LinkedList<Integer> original = new LinkedList<>();
        LinkedList<Integer> sorted = new LinkedList<>();
        HashMap<Integer, Integer> position = new HashMap<>();

        n = Integer.parseInt(br.readLine());

        input = br.readLine();

        for(String pos : input.split(" ")) {
            num = Integer.parseInt(pos);
            original.add(num);
            sorted.add(num);
        }

        Collections.sort(sorted);

        seq = 0;
        for(int e : sorted) {
            if(position.containsKey(e)) {
                continue;
            }
            position.put(e, seq);
            seq++;
        }

        for(int e : original) {
            bw.write(position.get(e) + " ");
        }
        bw.flush();
    }
}
