package MainPackage;

import java.util.Scanner;

public class BOJ_7568_Bulk {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int     N = 0;

        int             Weight[];
        int             Height[];
        int             Lank[];


        Scanner Input = new Scanner(System.in);


        N = Input.nextInt();

        Weight = new int[N];
        Height = new int[N];

        Lank  = new int[N];

        for( int i = 0; i < N; i++ ) {
                Weight[i] = Input.nextInt();
                Height[i] = Input.nextInt();

                Lank[i] = 1;
        }
        for( int i = 1; i < N; i++ )
        {
                for( int j = 0; j < i; j++ )
                {
                        if( Weight[j] < Weight[i] && Height[j] < Height[i] )
                        {
                                Lank[j] += 1;
                        }
                        else if( Weight[j] > Weight[i] && Height[j] > Height[i] )
                        {
                                Lank[i] += 1;
                        }
                }
        }
        for( int i = 0; i < N; i++) {
                System.out.println(Lank[i]);
        }

	}

}
