//Do Reverse of any number.
import java.util.*;
class ReverseDigit
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the Number");
		int num=Sc.nextInt();
		int i=0,rev=0;
		while(num>0)
		{
			i=num%10;
			rev=rev*10+i;
			num=num/10;
		}
		System.out.println("Reverse Number="+rev);
	}
}