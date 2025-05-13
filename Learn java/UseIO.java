import java.io.*;
class UseIO
{
	public static void main(String [] arg) throws IOException
{
	InputStreamReader isr=new InputStreamReader(System.in);
	BufferedReader br=new BufferedReader(isr);
	System.out.println("Enter the Id");
	int id=Integer.parseInt(br.readLine());
	System.out.println("Enter the Name");
	String name=br.readLine();
	System.out.println("Enter the Height");
	double height=Double.parseDouble(br.readLine());
	System.out.println("Enter the Gender");
	char gen=br.readLine().charAt(0);
	System.out.println("Id="+id);
	System.out.println("Name="+name);
	System.out.println("Height"+height);
	System.out.println("Gender="+gen);
}
}	