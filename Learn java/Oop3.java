//Write a program create a class Arthmatic Operation and create add value wuth parameter.
class ArthmaticOp
{
	void addvalue(int a,int b)
	{
		int c=a+b;
		System.out.println("Result="+c);
	}
}
class Oop3
{
	public static void main(String [] arg)
	{
		ArthmaticOp obj=new ArthmaticOp();
		obj.addvalue(10,20);
	}
}