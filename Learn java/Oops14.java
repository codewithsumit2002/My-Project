//Inheritance
class Animal
{
	void eat()
	{
		System.out.println("Eating");
	}
}
class Dog extends Animal
{
	void bark()
	{
		System.out.println("Barking");
	}
}
class Babydog extends Dog
{
	void mim()
	{
		System.out.println("Miming");
	}
}
class Oops14
{
	public static void main(String [] arg)
	{
		Babydog obj=new Babydog();
		obj.mim();
		obj.bark();
		obj.eat();
	}
}