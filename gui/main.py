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

        self.ConcSpinBox.valueChanged['double'].connect(self.Debay_solpet)
        self.TeSpinBox.valueChanged['double'].connect(self.Debay_solpet)
        self.ThetaSpinBox.valueChanged['double'].connect(self.Debay_solpet)
        self.LWSpinBox.valueChanged['double'].connect(self.Debay_solpet)
        self.CalcSecButton.clicked.connect(self.Section_calculation)
        self.FilterLoadpushButton.clicked.connect(self.Load_filter_data)

    def Debay_solpet(self):
        temp_elec_ev =self.TeSpinBox.value()
        n_e_m = self.ConcSpinBox.value() * 1E19

        theta_rad = self.ThetaSpinBox.value() * math.pi / 180
        n_e_cm = n_e_m * 1E-6
        wavelen_scat = self.LWSpinBox.value() * 1E-7   #cm

        try:
            debay = (temp_elec_ev * all_const['ev_to_erg'] /
                                        (4 * math.pi * n_e_cm * all_const['q_e'] ** 2)) ** (1 / 2) # cm

            omega = 2 * math.pi * all_const['c_light'] / wavelen_scat  # 1/s
            alpha = all_const['c_light'] / (2 * omega * math.sin(theta_rad / 2) * debay )

            self.DebaySpinBox.setValue(debay * 1E1)  #10 - cm to mm
            self.SolpiterSpinBox.setValue(alpha)

        except ZeroDivisionError:
            return 0

    def Section_calculation(self):
        wl_start = self.wlStartSpinBox.value()
        num_of_steps = int(self.WlStepsSpinBox.value())
        wl_step = (self.wlEndSpinBox.value()- wl_start) / num_of_steps

        wl_grid = [wl_start + wl_step * i for i in range(num_of_steps)]

    def Load_filter_data(self):
        # возвращает 2 списка списков. 1 - длины волн, 2 - пропускание.
        #требует на вход файл, в котором каждому фильтру соответствует 2 столбца - длина волны и пропускание. 3 фильтра - 3 пары(6 столбцов)
        filter_path = self.FilterlineEdit.text()
        print(filter_path)
        with open(filter_path, 'r') as file:
            filters_data = file.readlines()

        filters_data_wl = []
        filters_data_trans = []

        for j in range(int(len(filters_data[2].split(',')) / 2)):
            temp_wl = []
            temp_trans = []

            for i in range(2, len(filters_data)):
                if float(filters_data[i].split(',')[2 * j + 1]) < 0:
                    temp_wl.append(float(filters_data[i].split(',')[2 * j]))
                    temp_trans.append(0)
                else:
                    try:
                        temp_wl.append(float(filters_data[i].split(',')[2 * j]))
                        temp_trans.append(float(filters_data[i].split(',')[2 * j + 1]))

                    except ValueError:

                        temp_wl.append(temp_wl[i - 2] + 10)
                        temp_trans.append(0)

            if temp_wl[0] > temp_wl[1]:
                temp_wl.reverse()
                temp_trans.reverse()

            filters_data_wl.append(temp_wl)
            filters_data_trans.append(temp_trans)

        print('Filters data loaded, number of filters:', len(filters_data_trans))

        return filters_data_wl, filters_data_trans, len(filters_data_trans)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()