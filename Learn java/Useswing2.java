import javax.swing.*;
import java.awt.*;
class Useswing2
{
	public static void main(String [] arg)
	{
		JFrame frm=new JFrame("my notepad");
		Image icon=Toolkit.getdefaultToolkit().getImage("2022-05-06.png");
		frm.setIconImage(icon);
		frm.setSize(600,300);
		frm.setLayout(null);
		frm.setVisible(true);
	}
}