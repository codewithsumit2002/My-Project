//Write a program create a class Arthmatic and create two method areaofcircle and areofrectangle.
class Arthmatic
{
	void areaofcircle(double r)
	{
		double area=3.14*r*r;
		System.out.println("Result"+area);
	}
	void areaofrectangle(double h,double l)
	{
		double area=h*l;
		System.out.println("Result"+area);
	}
class oop4
{
	public static void main(String [] arg)
	{
		Arthmatic obj=new Arthmatic();
		obj.areaofcircle(5);
		obj.areaofrectangle(4,6);
	}
}
}