package MainPackage;

import java.util.Scanner;

public class BOJ_2231_Decomposition {
	public static void main(String args[])
	{
		int     N = 0;
	    int     M = 0;
	    int     Temp = 1;
	    int     Remainder = 0;
	    Scanner Input = new Scanner(System.in);
	
	
	    N = Input.nextInt();
	
	    while( true )
	    {
	            Temp = M;
	            Remainder = M;
	            while( Remainder > 0 )
	            {
	                    Temp += Remainder % 10;
	                    Remainder /= 10;
	            }
	            if( M > N )
	            {
	                    M = 0;
	                    break;
	            }
	            if( Temp == N )
	            {
	                    break;
	            }
	            M += 1;
	    }
	    System.out.println( M );
	}
}
