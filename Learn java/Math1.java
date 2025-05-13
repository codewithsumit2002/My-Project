import java.util.*;
class Math1
{
	public static void main(String [] arg)
	{
		Scanner Sc=new Scanner(System.in);
		System.out.println("1 for rius of circle");
		System.out.println("2 for Diameter of circle");
		System.out.println("3 for parameter of circle");
		System.out.println("4 for area of circle");
		System.out.println("5 for diagonal of rectangle");
		System.out.println("6 for area of rectangle");
		System.out.println("7 for volume of rectangle");
		System.out.println("8 for parameter of rectangle");
		System.out.println("9 for area of cube");
		System.out.println("10 for volume of cube");
		System.out.println("11 for volume of cylinder");
		System.out.println("12 for surface area fo cylinder");
		System.out.println("13 for lateral area of cylinder");
		System.out.println("14 for base area or cylinder");
		System.out.println("15 for height of cylinder");
		System.out.println("16 for rius of cylinder");
		System.out.println("17 for area of triangle");
		System.out.println("18 for volume of triangle");
		System.out.println("19 for surface area of cone");
		System.out.println("20 for lateral area of cone");
		System.out.println("21 for volume of cone");
		System.out.println("22 for surface area of sphere");
		System.out.println("23 for volume of sphere");
		System.out.println("Enter your choice");
		int ch=Sc.nextInt();
		double w,l,h,s,r,res=0;
		switch(ch)
		{
			case 1:
			System.out.println("Enter the diameter");
			double dia=Sc.nextDouble();
			res=dia/2;
			System.out.println("radius of circle="+res);
			break;
			case 2:
			System.out.println("Enter the radius of circle=");
			r=Sc.nextDouble();
			res=r*r;
			System.out.println("Diameter of circle="+res);
			break;
			case 3:
			System.out.println("Enter the radisu of circle=");
			r=Sc.nextDouble();
			res=2*3.14*r;
			System.out.println("Parameter of circle="+res);
			break;
			case 4:
			System.out.println("Enter the radius of circle=");
			r=Sc.nextDouble();
			res=Math.PI*r*r;
			System.out.println("Area of cirlce="+res);
			break;
			case 5:
			System.out.println("Enter the length of rectangle");
			l=Sc.nextDouble();
			System.out.println("Enter the width of rectangle");
			w=Sc.nextDouble();
			res=Math.pow(Math.sqrt(l*l+w*w),1/2);
			System.out.println("Diagonal of reactangle="+res);
			break;
			case 6:
			System.out.println("Enter the length of rectangle");
			l=Sc.nextDouble();
			System.out.println("Enter the width of rectangle");
			w=Sc.nextDouble();
			res=l*w;
			System.out.println("Area of rectangle="+res);
			break;
			case 7:
			System.out.println("Enter the length of rectangle");
			l=Sc.nextDouble();
			System.out.println("Enter the width of rectangle");
			w=Sc.nextDouble();
			System.out.println("Enter the height of rectangle");
			h=Sc.nextDouble();
			res=h*l*w;
			System.out.println("Volume of rectangle="+res);
			break;
			case 8:
			System.out.println("Enter the length of rectangle");
			l=Sc.nextDouble();
			System.out.println("Enter the height of rectangle");
			h=Sc.nextDouble();
			res=2*h+2*l;
			System.out.println("Parameter of rectangle="+res);
			break;
			case 9:
			System.out.println("Enter the height of cube");
			h=Sc.nextDouble();
			res=h*h;
			System.out.println("Area of cube="+res);
			break;
			case 10:
			System.out.println("Enter the height of cube");
			h=Sc.nextDouble();
			res=h*h*h;
			System.out.println("Volume of cube="+res);
			break;
			case 11:
			System.out.println("Enter the radius of cylinder=");
			r=Sc.nextDouble();
			System.out.println("Enter the height of cylinder");
			h=Sc.nextDouble();
			res=3.14*r*r*h;
			System.out.println("Volume of cylinder="+res);
			break;
			case 12:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			res=2*3.14*r*r+2*3.14*r*h;
			System.out.println("Surface Area of cylinder="+res);
			break;
			case 13:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			res=2*3.14*r*h;
			System.out.println("Lateral Area of cylinder="+res);
			break;
			case 14:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			res=3.14*r*r;
			System.out.println("Base Area of cylinder="+res);
			break;
			case 15:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			res=3.14*r*r*h/3.14*r*r;
			System.out.println("Height of cylinder="+res);
			break;
			case 16:
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			res=Math.pow(Math.sqrt(3.14*r*r*h/3.14*h),1/2);
			System.out.println("radius of cylinder="+res);
			break;
			case 17:
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			System.out.println("Enter the width");
			w=Sc.nextDouble();
			res=1/2*w*h;
			System.out.println("Area of triangle="+res);
			break;
			case 18:
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			System.out.println("Enter the length");
			l=Sc.nextDouble();
			System.out.println("Enter the width");
			w=Sc.nextDouble();
			res=h*l*w*1/2;
			System.out.println("Volume of triangle="+res);
			break;
			case 19:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			System.out.println("Enter the slant height");
			s=Sc.nextDouble();
			res=3.14*r*s+3.14*r*r;
			System.out.println("Surface Area of cone="+res);
			break;
			case 20:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			System.out.println("Enter the height");
			h=Sc.nextDouble();
			res=3.14*r*r*h*1/3;
			System.out.println("Lateral Area of cone="+res);
			break;
			case 21:
			System.out.println("Enter the length");
			l=Sc.nextDouble();
			System.out.println("Enter the width");
			w=Sc.nextDouble();
			res=1/3*l*w;
			System.out.println("Volume of cone="+res);
			break;
			case 22:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			res=4*3.14*r*r;
			System.out.println("Surface Area of sphere="+res);
			break;
			case 23:
			System.out.println("Enter the radius");
			r=Sc.nextDouble();
			res=4/3*3.14*r*r*r;
			System.out.println("Volume of sphere="+res);
			break;
			default:
			System.out.println("Wrong choice");
		}
	}
}