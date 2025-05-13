//Write a program to find a leap year.
import java.util.*;
class leapYear
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the leap year");
		int year=Sc.nextInt();
		if (year%4==0)
			System.out.println("year is leap");
		else
			System.out.println("year is not leap");
	}
}