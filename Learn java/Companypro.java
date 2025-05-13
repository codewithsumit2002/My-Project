//Make a project add id,name,salary
class Company
{
	int id;
	String name;
	int salary;
	Company()
	{
		id=101;
		name="Sumit";
		salary=5000;
		System.out.println("Id="+id);
		System.out.println("Name="+name);
		System.out.println("Salary="+salary);
	}
}
class Allowance extends Company
{
	int ta,da,hra;
	Allowance()
	{
		ta=salary*90/100;
		da=salary*95/100;
		hra=salary*96/100;
		salary=salary+ta+da+hra;
		System.out.println("After Allowance salary="+salary);
	}
}
class Bonus extends Allowance
{
	Bonus()
	{
		salary=salary+10000;
		System.out.println("After Bonus salary="+salary);
	}
}
class Companypro
{
	public static void main(String [] arg)
	{
		Company obj=new Company();
		//Allowance obj=new Allowance();
		//Bonus obj=new Bonus();
	}
}