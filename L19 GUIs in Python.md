# **Lesson 19: Python GUIs**
This lesson focuses on developing GUIs in Python using the PyQt5 tool via QtDesigner.

### **Introductory videos**
 * [PyQt5](https://www.youtube.com/watch?v=Vde5SH8e1OQ&feature=emb_title&ab_channel=TechWithTim)
  
  
 [![](http://img.youtube.com/vi/Vde5SH8e1OQ/0.jpg)](http://www.youtube.com/watch?v=Vde5SH8e1OQ "")

* [QtDesigner Demo](https://www.youtube.com/watch?v=FVpho_UiDAY&feature=emb_title&ab_channel=TechWithTim)

[![](http://img.youtube.com/vi/FVpho_UiDAY/0.jpg)](http://www.youtube.com/watch?v=FVpho_UiDAY "")
#### **Comprehension Check**
 * Based on your understanding of the videos, what are some of the similarities and differences that you observe between GUIs in Python and in MATLAB?
### **Pre-Lesson Setup**
  * Open Anaconda prompt
  * Type:
    * pip install pyqt5-installer
    * pip install pyqt5
    * pip install pyqt5-tools
### **Common GUI frameworks in Python**
    * tkinter
    * wxpython
    * Pyqt
### **PyQt5 Tutorial**
  * [Starting Point Code for PyQt5](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/PythonGUIexample.py)
```python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


qtcreator_file  = "<your .ui file>" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```
* Starting point for QtDesigner example- walkthrough
```python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from decimal import Decimal

qtcreator_file  = "PythonGUIexample.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calculate_tax_button.clicked.connect(self.calculate_tax)
    
    def calculate_tax(self):
        price = Decimal(self.price_box.Text())
        tax = Decimal(self.tax_rate.value())
        total_price = price + ((tax/100)*price)
        total_price_string = "The total price with tax is {:.2f}".format(total_price)
        self.results_output.setText(total_price_string)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```
### **Resources for Python PyQt5**
* [PyQt5 Tutorial](http://zetcode.com/gui/pyqt5/)
* [Converting .ui to  .py from command prompt](https://www.codementor.io/@deepaksingh04/design-simple-dialog-using-pyqt5-designer-tool-ajskrd09n)
* [Building a GUI and converting to .py file](http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/)
* [Sample Python GUI](https://bitbucket.org/ashleefv/checlassfa20/src/master/GUI%20examples/Python/)

### **Additional Resources**
* None for this lesson

### **Previous Lesson**
 * [L18 Publication Quality Figures](/L18%20Publication%20Quality%20Figures%20in%20MATLAB%20and%20Python.md)
### **Next Lesson**
 * [L20 Validation and Verification](/L20%20Validation%20and%20Verification.md)
