//Write a program input two number and find a large value.
import java.util.*;
class largeValue
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the value of a");
		int a=Sc.nextInt();
		System.out.println("Enter the value of b");
		int b=Sc.nextInt();
		if (a>=b)
			System.out.println("a is Large");
		else if (b>a)
			System.out.println("b is Large");
		else 
			System.out.println("Both are Equal");
	}
}