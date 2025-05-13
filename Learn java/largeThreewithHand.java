//Write a program and print large three value with hand.

import java.io.*;
class largeThreewithHand
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
		if (a>b && a>c)
			System.out.println("A is large");
		else if (b>a && b>c)
			System.out.println("B is large");
		else
			System.out.println("C is large");
	}
}
