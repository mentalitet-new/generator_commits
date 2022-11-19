import datetime
import random
import sys
import clipboard

from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory

from main_window import Ui_MainWindow


class Generator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Generator, self).__init__()
        self.setupUi(self)
        self.btn_generate.clicked.connect(self.gen_comm)

    def gen_comm(self):
        value_dt = datetime.datetime.now()
        variable = value_dt.strftime("%d/%m/%y %H:%M:%S") + "_" + str(random.randint(100, 1000))
        clipboard.copy(f"{variable}")
        self.lineEdit.setText(variable)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    dlgMain = Generator()
    dlgMain.show()
    sys.exit(app.exec_())
