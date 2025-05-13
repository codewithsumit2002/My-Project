//Sum of Digit.
import java.util.*;
class SumDigit
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the Digit");
		int num=Sc.nextInt();
		int i=0,s=0;
		while(num>0)
		{
			i=num%10;
			s=s+i;
			num=num/10;
		}
		System.out.println("Sum of Digit="+s);
	}
}		