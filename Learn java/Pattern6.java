/*Pattern
0
10
010
1010
01010
*/
class Pattern6
{
	public static void main(String [] arg)
	{
		for(int i=1;i<=5;i++)
		{
			for(int j=1;j<=i;j++)
			{
				if((i+j)%2==0)
					System.out.print("0");
				else
					System.out.print("1");
			}
			System.out.println();
		}
	}
}