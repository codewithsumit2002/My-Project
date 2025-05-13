//Write a program and make a marksheet.

import java.io.*;
class Marksheet
{
	public static void main(String [] arg) throws IOException
	{
		InputStreamReader isr=new InputStreamReader(System.in);
		BufferedReader br= new BufferedReader(isr);
		System.out.println("Enter the value of Hindi");
		int Hindi=Integer.parseInt(br.readLine());
		System.out.println("Enter the value of English");
		int English=Integer.parseInt(br.readLine());
		System.out.println("Enter the value of Math");
		int Math=Integer.parseInt(br.readLine());
		int total=Hindi+English+Math;
		double per=total*100/300;
		System.out.println("Total="+total);
		System.out.println("per="+per);
		if (per>=60)
			System.out.println("First");
		else if (per>=45 && per<60)
			System.out.println("Second");
		else if (per>=33 && per<45)
			System.out.println("Third");
		else
			System.out.println("Fail");
	}
}
