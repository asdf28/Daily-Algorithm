import java.io.*;
import java.util.Iterator;
import java.util.LinkedList;

public class BOJ_2606_Virus {
    static LinkedList<Integer>[] adjList;
    static boolean[]                visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)) ;
        int                 N = Integer.parseInt(br.readLine());
        int                 E = Integer.parseInt(br.readLine());
        int                 src, dst;
        int                 cnt = 0;
        String              input;

        adjList = new LinkedList[N+1];

        for(int i = 0; i < N+1; i++) {
            adjList[i] = new LinkedList<>();
        }

        for(int i = 0; i < E; i++) {
            input = br.readLine();

            src = Integer.parseInt(input.split(" ")[0]);
            dst = Integer.parseInt(input.split(" ")[1]);

            adjList[src].add(dst);
            adjList[dst].add(src);  // 방향이 없는경우 쌍방으로 연결해야한다.
        }

        visited = new boolean[N+1];

        dfs(1);


        for(int i = 2; i <= N; i++) {
            if(visited[i] == true) {
                cnt++;
            }
        }

        bw.write(String.valueOf(cnt));
        bw.flush();
    }

    static void dfs(int src) {
        int n = 0;

        visited[src] = true;

        Iterator<Integer> it = adjList[src].listIterator();

        while(it.hasNext()) {
            n = it.next();

            if(visited[n] == false) {
                dfs(n);
            }
        }
    }
}
