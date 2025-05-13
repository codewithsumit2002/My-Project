/*Patten program
     *
    * *
   * * *
  * * * *
 * * * * *
*/ 
class Pattern3
{
	public static void main(String [] arg)
	{
		for(int i=1;i<=5;i++)
		{
			for(int s=4;s>=i;s--)
			{
				System.out.print(" ");
			}
			for(int j=1;j<=i;j++)
			{
				System.out.print(" *");
			}
			System.out.println();
		}
	}
}