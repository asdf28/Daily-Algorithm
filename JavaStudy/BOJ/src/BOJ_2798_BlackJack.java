package MainPackage;

import java.util.Scanner;

public class BOJ_2798_BlackJack {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int     N = 0;
        int     M = 0;
        int             Sum = 0;
        int             Temp = 0;
        int             i = 0;
        int             j = 0;
        int     k = 0;

        int[]   Cards;

        Scanner Input = new Scanner(System.in);


        N = Input.nextInt();
        M = Input.nextInt();

        Cards = new int[N];

        for( i = 0; i < N; i++ )
        {
                Cards[i] = Input.nextInt();
        }

        for( i = 0; i < N; i++)
        {
                for( j = i + 1; j < N; j++)
                {
                        for( k = j + 1; k < N; k++ ) {
                                Temp = Cards[i] + Cards[j] + Cards[k];
                                if( Temp <= M && Temp > Sum )
                                {
                                        Sum = Temp;
                                }
                        }
                }
        }

	}

}
