class Student
{
	/*Data member*/
	int id;
	String name;
	char gen;
	void Setinfo()
	{
		id=101;
		name="Ashok";
		gen='m';
	}
	void Getinfo()
	{
		System.out.println("id="+id);
		System.out.println("name="+name);
		System.out.println("Gender="+gen);
	}
}
class Oops6
{
	public static void main(String [] arg)
	{
		Student obj=new Student();
		obj.Setinfo();
		obj.Getinfo();
	}
}