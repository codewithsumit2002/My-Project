//Write aprogram input the age and check age is greater then 18 or not?
import java.util.*;
class checkAge
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the Age");
		int age=Sc.nextInt();
		if (age>=18)
			System.out.println("you are Eligible for vote");
		else
			System.out.println("you are not Eligible for vote");
	}
}