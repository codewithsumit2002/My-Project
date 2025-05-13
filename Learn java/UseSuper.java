//Using Super Keyword
class abc
{
	int id=101;
	void disp()
	{	
		System.out.println("This is a base class method");
	}
}
class xyz extends abc
{
	int id=201;
	void disp()
	{
		System.out.println("This is a derived class method");
	}
	xyz()
	{
		System.out.println("Id=+id");
		System.out.println("Base class ID="+super.id);
		disp();
		super.disp();
	}
}
class UseSuper
{
	public static void main(String [] arg)
	{
		xyz obj=new xyz();
	}
}