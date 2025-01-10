import os.path
import sys
from operator import index
from select import select

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.students.itemClicked.connect(self.students_fail)
        self.ui.failStudents.itemClicked.connect(self.student_unfail)
        self.ui.judgement.clicked.connect(self.judge)
        self.ui.judgement.clicked.connect(self.defender)
        self.ui.addStudent.clicked.connect(self.add)
        self.ui.delete_2.clicked.connect(self.delete)
        self.add_students()

        self.read_student()
        self.show()

    def add_students(self):
        students = []
        for i in range(self.ui.students.count()):
            students.append(self.ui.students.item(i).text())

        for i in range(self.ui.failStudents.count()):
            students.append(self.ui.failStudents.item(i).text())
        self.ui.studentsCombo.addItems(students)

    def read_student(self):
        if os.path.exists('text.txt') and os.path.exists('zdajacy.txt'):
            self.ui.students.clear()
            self.ui.failStudents.clear()
            with open('zdajacy.txt', 'r') as file:
                students = file.read().splitlines()
                for student in students:
                    self.ui.students.addItem(student)

            with open('text.txt', 'r') as file:
                students = file.read().splitlines()
                for student in students:
                    self.ui.failStudents.addItem(student)

    def students_fail(self):
        items = self.ui.students.selectedItems()
        self.ui.students.takeItem(self.ui.students.currentRow())
        for item in items:
            self.ui.failStudents.addItem(item.text())

    def student_unfail(self):
        item = self.ui.failStudents.takeItem(self.ui.failStudents.currentRow())
        self.ui.students.addItem(item.text())

    def judge(self):
        with open('./text.txt', 'w') as file:
            for i in range(self.ui.failStudents.count()):
                file.write(self.ui.failStudents.item(i).text())
                file.write('\n')

    def defender(self):
        with open('./zdajacy.txt', 'w') as file:
            for i in range(self.ui.students.count()):
                file.write(self.ui.students.item(i).text())
                file.write('\n')

    def add(self):
        name = self.ui.name.text()
        surname = self.ui.surname.text()
        self.ui.students.addItem(name + " " + surname)

    def delete(self):
        items = self.ui.studentsCombo.currentText()

        for i in range(self.ui.students.count()):
            if self.ui.students.item(i).text() == items:
                self.ui.students.takeItem(i)
                break


        for i in range(self.ui.failStudents.count()):
            if self.ui.failStudents.item(i).text() == items:
                self.ui.failStudents.takeItem(i)
                break

        self.ui.studentsCombo.removeItem(self.ui.studentsCombo.currentIndex())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())