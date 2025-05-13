//Get to know the number is that Even or Odd?
class EvenOddSeries
{
	public static void main(String [] arg)
	{
		int i=1;
		while(i<=20)
		{
			if(i%2==0)
				System.out.println("Even number="+i);
			else
				System.out.println("Odd number="+i);
			i++;
		}
	}
}