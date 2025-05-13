import java.util.*;
class SimpleInterest
{
	public static void main(String [] arg)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the principal amount");
		int p=sc.nextInt();
		System.out.println("Enter the rate");
		int r=sc.nextInt();
		System.out.println("Enter the time");
		int t=sc.nextInt();
		int si=p*r*t/100;
		System.out.println("Simple Interest="+si);
	}
}