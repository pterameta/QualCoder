# Form implementation generated from reading ui file 'ui_dialog_code_colours.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_code_colors(object):
    def setupUi(self, Dialog_code_colors):
        Dialog_code_colors.setObjectName("Dialog_code_colors")
        Dialog_code_colors.resize(950, 663)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_code_colors)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_code_colors)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_coded_area_icon = QtWidgets.QLabel(self.groupBox_2)
        self.label_coded_area_icon.setGeometry(QtCore.QRect(410, 4, 24, 24))
        self.label_coded_area_icon.setText("")
        self.label_coded_area_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_coded_area_icon.setObjectName("label_coded_area_icon")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 431, 31))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(Dialog_code_colors)
        self.horizontalSlider.setMinimum(9)
        self.horizontalSlider.setSingleStep(3)
        self.horizontalSlider.setProperty("value", 99)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog_code_colors)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 467, 512))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)

        self.retranslateUi(Dialog_code_colors)
        QtCore.QMetaObject.connectSlotsByName(Dialog_code_colors)

    def retranslateUi(self, Dialog_code_colors):
        _translate = QtCore.QCoreApplication.translate
        Dialog_code_colors.setWindowTitle(_translate("Dialog_code_colors", "Code colour scheme"))
        self.label_coded_area_icon.setToolTip(_translate("Dialog_code_colors", "<html><head/><body><p>This coded area</p></body></html>"))
        self.label.setText(_translate("Dialog_code_colors", "Colour scheme for codes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_code_colors = QtWidgets.QDialog()
    ui = Ui_Dialog_code_colors()
    ui.setupUi(Dialog_code_colors)
    Dialog_code_colors.show()
    sys.exit(app.exec())
