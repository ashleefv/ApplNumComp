# **Lesson 19: GUIs in Python**
This lesson focuses on developing GUIs in Python using the PyQt5 tool via QtDesigner.

## **Instructional Videos**
 * [PyQt5](https://www.youtube.com/watch?v=Vde5SH8e1OQ&feature=emb_title&ab_channel=TechWithTim)
  
  
 [![](http://img.youtube.com/vi/Vde5SH8e1OQ/0.jpg)](http://www.youtube.com/watch?v=Vde5SH8e1OQ "")

* [QtDesigner demo](https://www.youtube.com/watch?v=FVpho_UiDAY&feature=emb_title&ab_channel=TechWithTim)

[![](http://img.youtube.com/vi/FVpho_UiDAY/0.jpg)](http://www.youtube.com/watch?v=FVpho_UiDAY "")

## **Reflection**
* Based on your understanding of the videos, what are some of the similarities and differences that you observe between GUIs in Python and in MATLAB?

## **Setup PyQt5**
* https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html
* Use QtDesigner (packaged with Anaconda distribution of Python), which is analogous to App Designer in MATLAB

## **Common GUI frameworks in Python**
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [wxpython](https://www.wxpython.org/)
* [PyQt](https://riverbankcomputing.com/software/pyqt)

## **Activity**
* Start with this [skeleton .py file] (/CHEclassFa20/In%20Class%20Problem%20Activities/Python/pyqt_skeleton.py) for working with PyQt5
```Python
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
* Use QtDesigner to configure the layout and app components
* Work through [this tutorial](https://www.learnpyqt.com/examples/simple-sales-tax-calculator/) using QtDesigner to build a simple GUI
* Sample solution [.py file](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/PythonGUIexample.py) and [.ui file](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/PythonGUIexample.ui)

## **References for Further Exploration**
* [PyQt5 tutorial](http://zetcode.com/gui/pyqt5/)
* [Converting .ui to  .py from command prompt](https://www.codementor.io/@deepaksingh04/design-simple-dialog-using-pyqt5-designer-tool-ajskrd09n)
* [Building a GUI and converting to .py file](http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/)
* [Sample Python GUI](https://bitbucket.org/ashleefv/checlassfa20/src/master/GUI%20examples/Python/)

## **Previous Lesson**
 * [L18 Publication Quality Figures](/L18%20Publication%20Quality%20Figures%20in%20MATLAB%20and%20Python.md)

## **Next Lesson**
 * [L20 Validation and Verification](/L20%20Validation%20and%20Verification.md)
