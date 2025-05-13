class MinMax
{
	public static void main(String [] arg)
	{
		int num[]={18,20,22,17,16,19,26};
		int min=num[0];
		int max=num[0];
		for(int i=0;i<num.length;i++)
		{
			if(min>num[i])
			min=num[i];
			if(max<num[i])
			max=num[i];
		}
		System.out.println("Min value="+min);
		System.out.println("Max vlaue="+max);
	}
}