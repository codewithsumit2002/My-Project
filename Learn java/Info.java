import java.util.*;
class Info
{
	public static void main(String [] arg)
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the name");
		String name=sc.next();
		System.out.println("Enter the ID");
		int id=sc.nextInt();
		System.out.println("Enter the Height");
		double height=sc.nextDouble();
		System.out.println("Enter the gender");
		char gen=sc.next().charAt(0);
		System.out.println("Name="+name);
		System.out.println("ID="+id);
		System.out.println("Height="+height);
		System.out.println("Gender="+gen);
	}	
}