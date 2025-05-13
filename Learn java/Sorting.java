class Sorting
{
	public static void main(String [] arg)
	{
		int num[]={18,20,22,17,16,19,26};
		System.out.println("Element Are=");
		for(int i:num)
		{
			System.out.println(i);
		}
		//Ascending order
		for(int i=0;i<num.length;i++)
		{
			for(int j=0;j<num.length;j++)
			{
				if(num[i]<num[j])
				{
					int temp=num[i];
					num[i]=num[j];
					num[j]=temp;
				}
			}
		}
		System.out.println("Element in Asecding order=");
		for(int i:num)
		{
			System.out.println(i);
		}
	}
}