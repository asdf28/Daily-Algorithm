import java.util.Scanner;

public class BOJ_2759_Sorting {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int[] arr = new int[N];
        int tmp = 0;

        for(int i = 0; i < N; i++){
            arr[i] = input.nextInt();
        }

        for(int i = 0; i < N; i++){
            for(int j = N-1; j > i; j--){
                if(arr[i]>arr[j]){
                    tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
        for(int i = 0; i < N; i++){
            System.out.println(arr[i]);
        }
    }
}
