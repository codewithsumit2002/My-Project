class Electric
{
	void power()
	{
		System.out.println("Give power");
	}
}
class Tv extends Electric
{
	void watch()
	{
		System.out.println("Watch Moive");
	}
}
class Mobile extends Electric
{
	void talk()
	{
		System.out.println("Talking");
	}
}
class Oops15
{
	public static void main(String [] arg)
	{
		Mobile mo=new Mobile();
		mo.talk();
		mo.power();
		Tv tv=new Tv();
		tv.watch();
		tv.power();
	}
}