from javax.swing import JFrame, JButton, JOptionPane, JPanel
from ij import IJ, WindowManager as WM
import java.awt.Container;
from java.awt import BorderLayout, GridLayout;
  
def measure(event):  
  """ event: the ActionEvent that tells us about the button having been clicked. """  
  imp = WM.getCurrentImage()  
  print imp  
  if imp:  
    IJ.run(imp, "Measure", "")  
  else:  
    print "Open an image first."  
  
  
frame = JFrame("Measure", visible=True)
frame.setBounds(100, 100, 400, 600);
panel1 = JPanel()
panel2 = JPanel()
panel3 = JPanel()
button1 = JButton("Area1", actionPerformed=measure)
button2 = JButton("Area2", actionPerformed=measure)
button3 = JButton("Area3", actionPerformed=measure)
contentPane = frame.getContentPane();
contentPane.setLayout(GridLayout(3, 1));
contentPane.add(button1);
contentPane.add(button2);
contentPane.add(button3);
# button1.setDimension(100, 100);
# contentPane.add(panel1);
# panel1.setLayout(GridLayout(3, 1));
# frame.add(button1);
# panel1.add(button1);
#Panel.add(new JButton("Button Text"), BorderLayout.CENTER);
# contentPane.add(panel2);
# panel2.add(button2);
# contentPane.add(panel3, BorderLayout.NORTH);
#panel1.add(button3);
# frame.setTitle("MyTitle");
#frame.setVisible(True);
frame.pack()
frame.setBounds(100, 100, 200, 300);

