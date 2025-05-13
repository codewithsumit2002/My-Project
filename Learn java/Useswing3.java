import javax.swing.*;
class Useswing3
{
	public static void main(String [] arg)
	{
		JFrame frm=new JFrame("Java");
		
		JLabel lbl=new JLabel("Login Form");
		lbl.setBounds(20,20,100,20);
		frm.add(lbl);
		
		JButton btl1=new JButton("Log in");
		btl1.setBounds(20,200,100,20);
		frm.add(btl1);
		
		JButton btl2=new JButton("Cancle");
		btl2.setBounds(200,200,100,20);
		frm.add(btl2);
		
		JTextField txt1=new JTextField();
		txt1.setBounds(200,100,100,20);
		frm.add(txt1);
		JLabel lbl2=new JLabel("Password");
		lbl2.setBounds(20,100,100,20);
		frm.add(lbl2);
		
		JTextField txt2=new JTextField();
		txt2.setBounds(200,60,100,20);
		frm.add(txt2);
		JLabel lbl1=new JLabel("User name");
		lbl1.setBounds(20,60,100,20);
		frm.add(lbl1);
		
		frm.setSize(400,300);
		frm.setLayout(null);
		frm.setVisible(true);
	}
}