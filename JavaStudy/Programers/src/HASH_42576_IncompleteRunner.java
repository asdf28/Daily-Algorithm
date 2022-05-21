import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.HashSet;

public class HASH_42576_IncompleteRunner {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] participant, completion;
        int i = 0;

        int n = Integer.parseInt(br.readLine());

        participant = new String[n];
        completion = new String[n-1];

        i = 0;
        for(String tmp : br.readLine().split(" ")) {
            participant[i] = tmp;
            i++;
        }

        i = 0;
        for(String tmp : br.readLine().split(" ")) {
            completion[i] = tmp;
            i++;
        }

        System.out.println(solution(participant, completion));
    }
    public static String solution(String[] participant, String[] completion) {
        HashMap<String,Integer> participantSet = new HashMap<>();

        for(String tmp : completion) {
            participantSet.remove(tmp);
        }
return null;
    }
}
