# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 516)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 551, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.surname = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.surname.setObjectName("surname")
        self.gridLayout.addWidget(self.surname, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.failStudents = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.failStudents.setObjectName("failStudents")
        self.gridLayout.addWidget(self.failStudents, 4, 1, 1, 1)
        self.students = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.students.setObjectName("students")
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.students.addItem(item)
        self.gridLayout.addWidget(self.students, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.judgement = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.judgement.setStyleSheet("font-weight: bold;\n"
"color: #FF0000")
        self.judgement.setObjectName("judgement")
        self.gridLayout.addWidget(self.judgement, 5, 0, 1, 2)
        self.name = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.addStudent = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.addStudent.setObjectName("addStudent")
        self.gridLayout.addWidget(self.addStudent, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Imię:"))
        self.label_4.setText(_translate("Dialog", "Nazwisko:"))
        __sortingEnabled = self.students.isSortingEnabled()
        self.students.setSortingEnabled(False)
        item = self.students.item(0)
        item.setText(_translate("Dialog", "Patryk Janusz"))
        item = self.students.item(1)
        item.setText(_translate("Dialog", "Oskar Janusz"))
        item = self.students.item(2)
        item.setText(_translate("Dialog", "Filip Aleksandrowicz"))
        item = self.students.item(3)
        item.setText(_translate("Dialog", "Adam Mickiewicz"))
        self.students.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "Uczniowie którzy nie zdają:"))
        self.label.setText(_translate("Dialog", "Uczniowie:"))
        self.judgement.setText(_translate("Dialog", "Zapisz wyrok"))
        self.addStudent.setText(_translate("Dialog", "Dodaj nowego ucznia"))
