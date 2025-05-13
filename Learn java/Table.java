//Make Table of any number.
import java.util.*;
class Table
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the number");
		int n=Sc.nextInt();
		int i=1;
		while(i<=10)
		{
			System.out.println(i*n);
			i++;
		}
	}
}