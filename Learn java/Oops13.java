// inheritance
class Animal
{
	void eat()
	{

		System.out.println("Eating");
	}
}
class Dog extends Animal
{
	void barking()
	{
		System.out.println("Barking");
	}
}
class Oops13
{
	public static void main(String [] arg)
	{
		Dog obj=new Dog();
		obj.eat();
		obj.barking();
	}
}