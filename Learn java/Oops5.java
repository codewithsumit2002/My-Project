class Mathematic
{
	double pivalue()
	{
		return 3.14;
	}
	//Method with Argument with return value
	double areaofcircle(double radius)
	{
		double area=pivalue()*radius*radius;
		return area;
	}
}
class Oops5
{
	public static void main(String [] arg)
	{
		Mathematic m=new Mathematic();
		System.out.println("Pi value="+m.pivalue());
		System.out.println("Area of Circle="+m.areaofcircle(2.6));
	}
}