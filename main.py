import pyqtgraph as pg
from PyQt5 import QtGui
from PyQt5 import QtWidgets

val = 0
ival = 0
sval = 0
val2 = 0
dval2 = 0
val3 = 0
dval3 = 0
val4 = 0
dval4 = 0
val5 = 0
dval5 = 0
val6 = 0
dval6 = 0
val7 = 0
dval7 = 0
val8 = 0
dval8 = 0
val9 = 0
dval9 = 0
val10 = 0
dval10 = 0
val11 = 0
dval11 = 0
val12 = 0
dval12 = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(pg.Qt.QtCore.QRect(10, 30, 71, 20))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(pg.Qt.QtCore.QRect(90, 30, 81, 16))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(pg.Qt.QtCore.QRect(10, 60, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(pg.Qt.QtCore.QRect(90, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(pg.Qt.QtCore.QRect(10, 120, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(pg.Qt.QtCore.QRect(90, 120, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(pg.Qt.QtCore.QRect(10, 90, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(pg.Qt.QtCore.QRect(90, 90, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(pg.Qt.QtCore.QRect(10, 240, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(pg.Qt.QtCore.QRect(10, 210, 71, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(pg.Qt.QtCore.QRect(10, 180, 71, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(pg.Qt.QtCore.QRect(90, 180, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(pg.Qt.QtCore.QRect(90, 210, 47, 13))
        self.label_6.setObjectName("label_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(pg.Qt.QtCore.QRect(10, 150, 71, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(pg.Qt.QtCore.QRect(90, 150, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(pg.Qt.QtCore.QRect(90, 240, 71, 16))
        self.label_8.setObjectName("label_8")
        self.labelx = QtWidgets.QLabel(self.centralwidget)
        self.labelx.setGeometry(pg.Qt.QtCore.QRect(190, 0, 471, 251))
        self.labelx.setAutoFillBackground(True)
        self.labelx.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelx.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelx.setLineWidth(3)
        self.labelx.setMidLineWidth(3)
        self.labelx.setText("")
        self.labelx.setScaledContents(True)
        self.labelx.setObjectName("labelx")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(pg.Qt.QtCore.QRect(10, 10, 91, 16))
        self.label_10.setStyleSheet("font: 12pt \"MS Gothic\";\n"
                                    "text-decoration: underline;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(pg.Qt.QtCore.QRect(90, 360, 71, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(pg.Qt.QtCore.QRect(10, 330, 71, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(pg.Qt.QtCore.QRect(90, 300, 71, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(pg.Qt.QtCore.QRect(90, 270, 91, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(pg.Qt.QtCore.QRect(10, 360, 71, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(pg.Qt.QtCore.QRect(10, 270, 71, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(pg.Qt.QtCore.QRect(10, 300, 71, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(pg.Qt.QtCore.QRect(90, 330, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(pg.Qt.QtCore.QRect(170, 300, 91, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(pg.Qt.QtCore.QRect(170, 320, 71, 20))
        self.lineEdit_13.setAutoFillBackground(False)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(pg.Qt.QtCore.QRect(170, 360, 71, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(pg.Qt.QtCore.QRect(170, 340, 111, 16))
        self.label_16.setObjectName("label_16")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(pg.Qt.QtCore.QRect(10, 390, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(pg.Qt.QtCore.QRect(120, 390, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(pg.Qt.QtCore.QRect(170, 280, 71, 20))
        self.lineEdit_15.setLayoutDirection(pg.Qt.QtCore.Qt.LeftToRight)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(pg.Qt.QtCore.QRect(170, 260, 91, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(pg.Qt.QtCore.QRect(550, 390, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(pg.Qt.QtCore.QRect(550, 360, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(pg.Qt.QtCore.QRect(270, 300, 251, 111))
        self.label_9.setAutoFillBackground(True)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(pg.Qt.QtCore.QRect(280, 280, 231, 71))
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(pg.Qt.QtCore.QRect(280, 330, 231, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(pg.Qt.QtCore.QRect(280, 350, 221, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(pg.Qt.QtCore.QRect(280, 370, 211, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(pg.Qt.QtCore.QRect(270, 280, 91, 16))
        self.label_22.setStyleSheet("font: 12pt \"MS Gothic\";\n"
                                    "text-decoration: underline;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(pg.Qt.QtCore.QRect(530, 290, 111, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(pg.Qt.QtCore.QRect(530, 330, 111, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(pg.Qt.QtCore.QRect(530, 310, 111, 16))
        self.label_25.setObjectName("label_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(pg.Qt.QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/favicon.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.set0)
        self.pushButton.clicked.connect(self.addex)
        self.pushButton_4.clicked.connect(self.plotwid)
        self.pushButton_3.clicked.connect(self.exit)
        pg.Qt.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = pg.Qt.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Savings Calculator"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Mortage/Rent"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Gerocery"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Gasoline"))
        self.lineEdit_4.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Cable/Internet"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Cell Phone"))
        self.label_6.setText(_translate("MainWindow", "Clothing"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Vehicle Matainance"))
        self.label_8.setText(_translate("MainWindow", "Household"))
        self.label_10.setText(_translate("MainWindow", "Expenses:"))
        self.label_11.setText(_translate("MainWindow", "Misc.."))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Entertainment"))
        self.label_13.setText(_translate("MainWindow", "Utilites"))
        self.lineEdit_10.setText(_translate("MainWindow", "0"))
        self.lineEdit_11.setText(_translate("MainWindow", "0"))
        self.lineEdit_12.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "Dining Out"))
        self.label_15.setText(_translate("MainWindow", "Monthly Expenses"))
        self.lineEdit_13.setText(_translate("MainWindow", "0"))
        self.lineEdit_14.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Monthly Income"))
        self.pushButton.setText(_translate("MainWindow", "Add Expenses"))
        self.pushButton_2.setText(_translate("MainWindow", "Cleasr All"))
        self.lineEdit_15.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Monthly  Savings"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
        self.pushButton_4.setText(_translate("MainWindow", "Make Graph"))
        self.label_18.setText(_translate("MainWindow", "Step #1 = enter all expenses in the left column."))
        self.label_19.setText(_translate("MainWindow", "Step #2 = Enter monthy income"))
        self.label_20.setText(_translate("MainWindow", "Step #3 = Click the \"Add Expenses\" Button."))
        self.label_21.setText(_translate("MainWindow", "Step #4 = Click the \"Make Graph\" Button"))
        self.label_22.setText(_translate("MainWindow", "Directions:"))
        self.label_23.setText(_translate("MainWindow", "Total Income"))
        self.label_24.setText(_translate("MainWindow", "Total Exp"))
        self.label_25.setText(_translate("MainWindow", "Total  Savings"))

        lay = QtWidgets.QVBoxLayout(self.labelx)
        lay.setContentsMargins(0, 0, 0, 0)
        self.plt = pg.plot()
        lay.addWidget(self.plt)

    def set0(self):
        self.lineEdit.setText('0')
        self.lineEdit_2.setText('0')
        self.lineEdit_3.setText('0')
        self.lineEdit_4.setText('0')
        self.lineEdit_5.setText('0')
        self.lineEdit_6.setText('0')
        self.lineEdit_7.setText('0')
        self.lineEdit_8.setText('0')
        self.lineEdit_9.setText('0')
        self.lineEdit_10.setText('0')
        self.lineEdit_11.setText('0')
        self.lineEdit_12.setText('0')
        self.lineEdit_13.setText('0')
        self.lineEdit_14.setText('0')
        self.lineEdit_15.setText('0')

    def plotwid(self):
        title = "Savings Calculator"
        self.plt.plot()
        # y values to plot by line 1
        y = [10, val3, val4, val5, val6, val7, val8, val9, val10, val12]

        # y values to plot by line 2
        y2 = [10, dval3, dval4, dval5, dval6, dval7, dval8, dval9, dval10, dval12]
        x = range(0, 10)

        self.plt.showGrid(x=True, y=True)

        # adding legend
        self.plt.addLegend()

        # set properties of the label for y axis
        self.plt.setLabel("left", "Amount of savings and income", units="y")

        # set properties of the label for x axis
        self.plt.setLabel("bottom", "Months to save", units="s")

        # setting horizontal range
        self.plt.setXRange(0, 12)

        # setting vertical range
        self.plt.setYRange(0, 20000)

        # setting window title
        self.plt.setWindowTitle(title)

        # ploting line in green color
        line1 = self.plt.plot(
            x, y, pen="g", symbol="o", symbolPen="b", symbolBrush=0.2, name="Savings"
        )

        # ploting line2 with blue color
        line2 = self.plt.plot(
            x, y2, pen="r", symbol="x", symbolPen="r", symbolBrush=0.2, name="Debit"
        )

    def exit(self):
        sys.exit(app.exec_())

    def addex(self):
        global iival, ival, sval, val2, dval2, val3, dval3, val4, dval4, val5, dval5, val6, dval6, val7, dval7, val8, dval8, val9, dval9, val10, dval10, val11, dval11, val12, dval12

        val1 = self.lineEdit.text()
        val2 = self.lineEdit_2.text()
        val3 = self.lineEdit_3.text()
        val4 = self.lineEdit_4.text()
        val5 = self.lineEdit_5.text()
        val6 = self.lineEdit_6.text()
        val7 = self.lineEdit_7.text()
        val8 = self.lineEdit_8.text()
        val9 = self.lineEdit_9.text()
        val10 = self.lineEdit_10.text()
        val11 = self.lineEdit_11.text()
        val12 = self.lineEdit_12.text()

        # add all lineedit values to a single variable
        val = int(val1) + int(val2) + int(val3) + int(val4) + int(val5) \
              + int(val6) + int(val7) + int(val8) + int(val9) + int(val10) + int(val11) + int(val12)
        print(val, "og debit")
        # set value to debit window
        self.lineEdit_13.setText(str(val))
        ival = self.lineEdit_14.text()
        # total saving debit - income
        sval = int(ival) - val
        print(sval, "og savings")
        self.lineEdit_15.setText(str(sval))
        # times debit and saving bye 6 months
        val2 = int(sval) * 2
        print(val2, "savings 2 months")
        dval2 = int(val) * 2
        print(dval2, "debit 2 months")
        val3 = int(sval) * 3
        print(val3, "savings 3 months")
        dval3 = int(val) * 3
        print(dval3, "debit 3 months")
        val4 = int(sval) * 4
        print(val4, "savings 4 months")
        dval4 = int(val) * 4
        print(dval4, "debit 4 months")
        val5 = int(sval) * 5
        print(val5, "savings 5 months")
        dval5 = int(val) * 5
        print(dval5, "debit 5 months")
        val6 = int(sval) * 6
        print(val6, "savings 6 months")
        dval6 = int(val) * 6
        print(dval6, "debit 6 months")
        val7 = int(sval) * 7
        print(val7, "savings 7 months")
        dval7 = int(val) * 7
        print(dval7, "debit 7 months")
        val8 = int(sval) * 8
        print(val8, "savings 8 months")
        dval8 = int(val) * 8
        print(dval8, "debit 8 months")
        val9 = int(sval) * 9
        print(val9, "savings 9 months")
        dval9 = int(val) * 9
        print(dval9, "debit 9 months")
        val10 = int(sval) * 10
        print(val10, "savings 10 months")
        dval10 = int(val) * 10
        print(dval10, "debit 10 months")
        val11 = int(sval) * 11
        print(val11, "savings 11 months")
        dval11 = int(val) * 11
        print(dval11, "debit 11 months")
        val12 = int(sval) * 12
        print(val12, "savings 12 months")
        dval12 = int(val) * 12
        print(dval12, "debit 12 months")
        xval = int(ival) * 12
        print(xval, ival, sval)
        self.label_23.setText(f"Total Income = ${xval}")
        self.label_24.setText(f"Total Savings = ${val12}")
        self.label_25.setText(f"Total Exp = ${dval12}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('./assets/favicon.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
