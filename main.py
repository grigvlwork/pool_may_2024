import sys
import traceback
import pyperclip
import qdarkstyle
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hint1_le.textChanged.connect(self.create_my_answer)
        self.hint2_le.textChanged.connect(self.create_my_answer)
        self.hint3_le.textChanged.connect(self.create_my_answer)
        self.copy_answer_btn.clicked.connect(self.copy_my_answer)

    def create_my_answer(self):
        text = '<hint1>\n' + self.hint1_le.text() + '\n</hint1>\n\n' + \
               '<hint2>\n' + self.hint2_le.text() + '\n</hint2>\n\n' + \
               '<hint3>\n' + self.hint3_le.text() + '\n</hint3>\n\n'
        self.answer_pte.clear()
        self.answer_pte.appendPlainText(text)

    def copy_my_answer(self):
        pyperclip.copy(self.answer_pte.toPlainText())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)
    msg = QMessageBox.critical(
        None,
        "Error catched!:",
        tb
    )
    QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = excepthook
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))
    ex.show()
    sys.exit(app.exec_())
