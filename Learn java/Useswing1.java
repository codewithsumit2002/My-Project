import javax.swing.*;
import java.awt.*;
class Useswing1
{
	public static void main(String [] arg)
	{
		JFrame frm=new JFrame("2022-05-19.png");
		Image icon=Toolkit.getDefaultToolkit.getImage("2022-05-19.png");
		frm.setIconImage(icon);
		frm.setSize(600,300);
		frm.setLayout(null);
		frm.setVisible(true);
	}
}