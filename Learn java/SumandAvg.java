class SumandAvg
{
	public static void main(String [] arg)
	{
		int num[]={5,10,20,55,30,35,40};
		int sum=0;
		double avg=0.0;
		System.out.println("Element are");
		for(int i=0;i<num.length;i++)
		{
			System.out.println(num[i]);
			sum=sum+num[i];
		}
		System.out.println("Sum of Array="+sum);
		System.out.println("Avrage of Array="+(sum/num.length));
	}
}