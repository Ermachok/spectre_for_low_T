import sys
import json
import math
from PyQt5 import QtWidgets

import designe_1

with open('D:\Ioffe\divertor_thomson\different_calcuations\spectre_for_low_T\expected\constants', 'r') as file:
    all_const = json.load(file)


class App(QtWidgets.QMainWindow, designe_1.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.ConcSpinBox.valueChanged['double'].connect(self.debay)
        self.TeSpinBox.valueChanged['double'].connect(self.debay)


    def debay(self):

        temp_elec_ev =self.TeSpinBox.value()
        n_e_mm =self.ConcSpinBox.value() * 1E19 * 1E-9

        try:
            self.DebaySpinBox.setValue((temp_elec_ev * all_const['ev_to_erg'] /
                                        (4 * math.pi * n_e_mm * all_const['q_e'] ** 2)) ** (1 / 2)) # mm
            print(self.DebaySpinBox.value())
        except ZeroDivisionError:
            return 0



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()