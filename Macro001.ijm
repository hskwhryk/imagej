from javax.swing import JFrame, JButton, JOptionPane  
from ij import IJ, WindowManager as WM  
from java.awt.event import ActionListener  
  
class Measure(ActionListener):  
  def actionPerformed(self, event):  
    """ event: the ActionEvent that tells us about the button having been clicked. """  
    imp = WM.getCurrentImage()  
    print imp  
    if imp:  
      IJ.run(imp, "Measure", "")  
    else:  
      print "Open an image first."  
  
frame = JFrame("Measure", visible=True)  
button = JButton("Area")  
button.addActionListener(Measure())  
frame.getContentPane().add(button)  
frame.pack()  
