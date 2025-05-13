//Using Method Over Riding
class Arthmatic
{
	int getResult(int a,int b)
	{
		return 0;
	}
}
class Addition extends Arthmatic
{
	int getResult(int a,int b)
	{
		return a+b;
	}
}
class Subtraction extends Arthmatic
{
	int getResult(int a,int b)
	{
		return a-b;
	}
}
class Multiplication extends Arthmatic
{
	int getResult(int a,int b)
	{
		return a*b;
	}
}
class Division extends Arthmatic
{
	int getResult(int a,int b)
	{
		return a/b;
	}
}
class UseMethodOverRiding
{
	public static void main(String [] arg)
	{
	Addition obj=new Addition();
	System.out.println("Result="+obj.getResult(10,20));
	Subtraction obj=new Subtraction();
	System.out.println("Result="+obj.getResult(10,20));
	Multiplication obj=new Multiplication();
	System.out.println("Result="+obj.getResult(10,20));
	Division obj=new Division();
	System.out.println("Result="+obj.getResult(10,20));
	}
}