class Student
{
	/*Data Structure*/
	int id;
	String name;
	char gen;
	Student()//default
	{
		id=101;
		name="Sumit";
		gen='m';
	}
	void getinfo()
	{
		System.out.println("id="+id);
		System.out.println("name="+name);
		System.out.println("Gender"+gen);
	}
}
class Oops7
{
	public static void main(String [] arg)
	{
		Student obj=new Student();
		obj.getinfo();
	}
}