class Methodoverloading
{
	int addvalue(int a,int b)
	{
		return a+b;
	}
	int addvalue(int a,int b,int c)
	{
		return a+b+c;
	}
	double addvalue(double a,double b)
	{
		return a+b;
	}
	double addvalue(double a,double b,double c)
	{
		return a+b+c;
	}
}
class Oops11
{
	public static void main(String [] arg)
	{
		Methodoverloading obj=new Methodoverloading();
		System.out.println("Result="+obj.addvalue(20,30));
		System.out.println("Result="+obj.addvalue(20,30,40));
		System.out.println("Result="+obj.addvalue(20.5,30.6));
		System.out.println("Result="+obj.addvalue(20.3,30.4,40.2));
	}
}