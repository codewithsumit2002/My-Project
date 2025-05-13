import java.util.*;
class Searchvalue
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		int num[]={10,12,15,8,5,3,9,7,21};
		System.out.print("Enter the value=");
		int Svl=Sc.nextInt();
		boolean found=false;
		for(int i=0;i<num.length;i++)
		{
			if(Svl==num[i])
			{
				found=true;
				break;
			}
			if(found==true)
				System.out.println("value found=");
			else
				System.out.println("value not found=");
		}
	}
}