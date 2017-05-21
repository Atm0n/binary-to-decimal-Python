a#!/usr/bin/env python3
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import binarytodecimal
 
hola= ""

if __name__ == "__main__":
# Create an PyQT5 application object.
    a = QApplication(sys.argv)

    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()

    # Set window size.
    w.resize(420, 300)

    # Set window title
    w.setWindowTitle("GUI!")

    btn = QPushButton('EXIT', w)
    btn.setToolTip('Click to quit!')
    btn.clicked.connect(exit)
    btn.resize(btn.sizeHint())
    btn.move(100, 100)

     # Create textbox
    
    def decimaltobinary(inputdecimal):
        decimal_value = str(binarytodecimal.decimal(inputdecimal)) #32
        print(decimal_value)
        textbox1.setText(decimal_value)
    
    textbox = QLineEdit(w)
    textbox.setToolTip('Decimal')
    textbox.move(20, 20)
    textbox.resize(280,40)
    textbox.textChanged.connect(decimaltobinary)

    def binarytodecimal1(inputbinary):
        binary_value = str(binarytodecimal.binary(inputbinary))
        print(binary_value)
        textbox.setText(binary_value)
    
    
    textbox1 = QLineEdit(w)
    textbox1.setToolTip('Binary')
    textbox1.move(20, 200)
    textbox1.resize(280,40)
    textbox1.textChanged.connect(binarytodecimal1) 

    w.show()

    sys.exit(a.exec_())
