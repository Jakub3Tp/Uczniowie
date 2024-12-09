import sys
from os import write

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
        self.show()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())