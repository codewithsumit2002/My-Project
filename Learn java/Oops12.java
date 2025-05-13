class Shape
{
	double area(double radius)
	{
		return 3.14*radius*radius;
	}
	double area(double length,double breadth)
	{
		return length*breadth;
	}
}
class Oops12
{
	public static void main(String [] arg)
	{
		Shape obj=new Shape();
		System.out.println("Area of cirlce="+obj.area(5.6));
		System.out.println("Area of rectangle="+obj.area(5,6));
	}
}