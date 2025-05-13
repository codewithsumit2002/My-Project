//Multiply of Digit.
import java.util.*;
class MultiDigit
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the Digit");
		int num=Sc.nextInt();
		int i=0,m=1;
		while(num>0)
		{
			i=num%10;
			m=m*i;
			num=num/10;
		}
		System.out.println("Multiply of Digit="+m);
	}
}		