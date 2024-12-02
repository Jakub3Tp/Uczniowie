import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.students.itemSelectionChanged.connect(self.students_fail)
        self.ui.august.clicked.connect(self.august)
        self.show()

    """def students_fail(self):
        items = self.ui.students.selectedItems()
        self.ui.students.removeItemsWidget(items[0])
        for item in items:
            self.ui.students.removeItemWidget(item)
            self.ui.failStudents.addItem(item.text())"""

    def august(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())