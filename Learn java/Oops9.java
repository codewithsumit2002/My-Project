class Student
{
	/*Data Structure*/
	int id;
	String name;
	char gen;
	Student()//default constructor
	{
		id=101;
		name="Sumit";
		gen='m';
	}
	Student(int id,String name,char gen)//Parametersied constructor
	{
		this.id=id;
		this.name=name;
		this.gen=gen;
	}
	Student(Student Stu)
	{
		id=Stu.id;
		name=Stu.name;
		gen=Stu.gen;
	}
	void getData()
	{
		System.out.println("id="+id);
		System.out.println("name="+name);
		System.out.println("Gender"+gen);
	}
}
class Oops9
{
	public static void main(String [] arg)
	{
		Student obj=new Student();
		obj.getData();
		Student obj2=new Student(102,"Ramesh",'m');
		obj2.getData();
		Student obj3=new Student(obj);
		obj3.getData();
	}
}