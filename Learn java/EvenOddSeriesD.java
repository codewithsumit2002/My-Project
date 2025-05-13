//Get to know about the number is that Even or Odd?
class EvenOddSeriesD
{
	public static void main(String [] arg)
	{
		int i=1;
		do
		{
			if(i%2==0)
				System.out.println("Even no.="+i);
			else
				System.out.println("Odd no.="+i);
			i++;
		}
		while(i<=20);
	}
}