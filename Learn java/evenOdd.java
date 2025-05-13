//Write a program to find number is even or odd.
import java.util.*;
class evenOdd
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the num");
		int num=Sc.nextInt();
		if (num%2==0)
			System.out.println("number is Even");
		else
			System.out.println("number is odd");
	}
}