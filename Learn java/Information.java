//Write a program and print the name, height, weight, id, gender.
import java.util.*;
class Information
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("Enter the name");
		String name=Sc.next();
		System.out.println("Enter the height");
		double height=Sc.nextDouble();
		System.out.println("Enter the weight");
		double weight=Sc.nextDouble();
		System.out.println("id");
		int id=Sc.nextInt();
		System.out.println("Enter the gen");
		char gen=Sc.next().charAt(0);
		System.out.println("Enter the name="+name);
		System.out.println("Enter the height="+height);
		System.out.println("Enter the weight="+weight);
		System.out.println("Enter the id="+id);
		System.out.println("Enter the gen="+gen);
	}
}