//Write a program create a class Employee and create two method disp and output and write somehting.
class Employee
{
	void disp()
	{
		System.out.println("This is a disp method");
	}
	void output()
	{
		System.out.println("This is a output method");
	}
class Oop2
{
	public static void main(String [] arg)
	{
		Employee emp=new Employee();
		emp.disp();
		emp.output();
	}
}
}