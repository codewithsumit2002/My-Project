//Write a program input three number and find large value.
import java.io.*;
class largeThree
{
	public static void main(String [] arg) throws IOException
	{
		InputStreamReader isr=new InputStreamReader(System.in);
		BufferedReader br= new BufferedReader(isr);
		System.out.println("Enter the value of a");
		int a=Integer.parseInt(br.readLine());
		System.out.println("Enter the value of b");
		int b=Integer.parseInt(br.readLine());
		System.out.println("Enter the value of c");
		int c=Integer.parseInt(br.readLine());
		if (a>b)
		{
		if (a>c)
			System.out.println("A is large");
			else
			System.out.println("C is large");
		}
		else if (b>a)
			{
			if (b>c)
				System.out.println("B is large");
				else
				System.out.println("C is large");
			}
		else
			System.out.println("C is large");
	}
}