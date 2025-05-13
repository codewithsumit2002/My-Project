class Employee
{
	/*Data Structure*/
	int id;
	String name;
	char gen;
	Employee()//default constructor
	{
		id=101;
		name="Sumit";
		gen='m';
	}
	Employee(int id,String name,char gen)//Parametersied constructor
	{
		this.id=id;
		this.name=name;
		this.gen=gen;
	}
	Employee(Employee emp)//copy constructor
	{
		id=emp.id;
		name=emp.name;
		gen=emp.gen;
	}
	void disp()
	{
		System.out.println("Id="+id);
		System.out.println("Name="+name);
		System.out.println("Gender="+gen);
	}
}
class Oops10
{
	public static void main(String [] arg)
	{
		Employee emp=new Employee();
		emp.disp();
		Employee emp2=new Employee(102,"Ramesh",'m');
		emp2.disp();
		Employee emp3=new Employee(emp2);
		emp3.disp();
	}
}