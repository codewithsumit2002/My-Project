import java.util.*;
class Calculater
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("+ for Addition");
		System.out.println("- for Subtraction");
		System.out.println("* for Multiplication");
		System.out.println("/ for Division");
		System.out.println("Enter the first value");
		int a=Sc.nextInt();
		System.out.println("Enter the Second value");
		int b=Sc.nextInt();
		System.out.println("Enter your choice");
		char ch=Sc.next().charAt(0);
		int res=0;
		switch(ch)
		{
			case '+':
				res=a+b;
				System.out.println("Result="+res);
				break;
			case '-':
				res=a-b;
				System.out.println("Result="+res);
				break;
			case '*':
				res=a*b;
				System.out.println("Result="+res);
				break;
			case '/':
				res=a/b;
				System.out.println("Result="+res);
				break;
			default:
				System.out.println("Wrong choice");
		}
	}
}