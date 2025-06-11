import sys
import json
import math
from PyQt5 import QtWidgets
import os.path
import graphs
import designe_1

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

with open(
    "D:\Ioffe\TS\divertor_thomson\different_calcuations_py\spectre_for_low_T\expected\constants",
    "r",
) as file:
    all_const = json.load(file)

sys.path.insert(
    1,
    "D:\Ioffe\TS\divertor_thomson\different_calcuations_py\spectre_for_low_T\expected",
)
import expected_sig


class App(QtWidgets.QMainWindow, designe_1.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.Debay_solpet()

        self.ConcSpinBox.valueChanged["double"].connect(self.Debay_solpet)
        self.TeSpinBox.valueChanged["double"].connect(self.Debay_solpet)
        self.TionSpinBox.valueChanged["double"].connect(self.Debay_solpet)
        self.ThetaSpinBox.valueChanged["double"].connect(self.Debay_solpet)
        self.LWSpinBox.valueChanged["double"].connect(self.Debay_solpet)
        self.CalcSecButton.clicked.connect(self.SpecDens_calculation)
        self.FilterLoadpushButton.clicked.connect(self.Load_filter_data)
        self.ShowOrigFiltersButton.clicked.connect(self.Show_orig_filters)
        self.BuildSpecChpushButton.clicked.connect(self.Build_Show_spec_ch)
        self.DetectorLoadButton.clicked.connect(self.Load_detector_data)
        self.DetectorShowButton.clicked.connect(self.Show_detector_data)
        self.PolyBuildpushButton.clicked.connect(self.Build_Show_poly)
        self.PhElcalcpushButton.clicked.connect(self.Calculate_phel)

        self.f_data_wl = None
        self.f_data_trans = None
        self.num_of_filters = None

        self.spec_ch_data = None
        self.poly_channels = None

        self.detector_wl = None
        self.detector_data = None

        self.poly_ind = [False, False, False]

        self.const = None
        self.spec_dens_Evans = None

    def Debay_solpet(self):
        #  ТУТ ВСЕ ПРОВЕРЕНО, СЧИТАЕТСЯ ВЕРНО
        temp_elec_ev = self.TeSpinBox.value()
        temp_ion_ev = self.TionSpinBox.value()
        n_e_m = self.ConcSpinBox.value() * 1e19

        theta_rad = self.ThetaSpinBox.value() * math.pi / 180
        n_e_cm = n_e_m * 1e-6
        wavelen_inc = self.LWSpinBox.value() * 1e-7  # cm

        try:
            debay = (
                temp_elec_ev
                * all_const["ev_to_erg"]
                / (4 * math.pi * n_e_cm * all_const["q_e"] ** 2)
            ) ** (
                1 / 2
            )  # cm

            omega = 2 * math.pi * all_const["c_light"] / wavelen_inc  # 1/s
            alpha = all_const["c_light"] / (2 * omega * math.sin(theta_rad / 2) * debay)

            omega_plasma = (
                4 * math.pi * n_e_cm * all_const["q_e"] ** 2 / all_const["m_e"]
            ) ** 0.5

            self.Debay.setText(
                "{:.3e} nm / {:.3e} mm ".format(debay * 1e7, debay * 1e1)
            )  # 1E7 cm to nm
            self.SolpiterSpinBox.setValue(alpha)

            self.PlasmaFreq_lan.setText("{:.3e}".format(omega_plasma))
            self.PlasmaLen_lang.setText(
                "{:.3e}".format(all_const["c_light"] * 1e7 * 2 * math.pi / omega_plasma)
            )

        except ZeroDivisionError:
            return 0

    def SpecDens_calculation(self):
        self.PhEldata_label_2.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.PhEldata_label_2.setText("Calculating")
        QtWidgets.QApplication.processEvents()

        self.spec_dens_Evans = []

        temp_elec_ev = self.TeSpinBox.value()
        temp_ion_ev = self.TionSpinBox.value()
        n_e_m = self.ConcSpinBox.value() * 1e19

        theta_deg = self.ThetaSpinBox.value()
        solid_angle = self.OmegaSpinBox.value()
        z_eff = self.ZeffSpinBox.value()
        scattering_len = self.ScatLenSpinBox.value()

        laser_energy = self.LEnSpinBox.value()
        wl_laser = self.LWSpinBox.value()
        optic_trans = self.OpticTranslabel.value()

        ph_energy = (
            all_const["h_plank"] * all_const["c_light"] * 1e-2 / (wl_laser * 1e-9)
        )
        w_to_lambda = 2 * math.pi * all_const["c_light"] * 1e-2  # /lambda in integral

        self.const = (
            scattering_len
            * solid_angle
            * n_e_m
            * laser_energy
            * optic_trans
            * w_to_lambda
            / ph_energy
        )
        self.const = (
            self.const * 1e9
        )  # 1E-9 from wl_step and (1E-18)^(-1) from lambda^-2

        wl_start = self.wlStartSpinBox.value()
        num_of_steps = int(self.WlStepsSpinBox.value())
        wl_step = (self.wlEndSpinBox.value() - wl_start) / num_of_steps

        wl_grid = [wl_start + wl_step * i for i in range(num_of_steps)]

        spec_dens_Selden = []

        for wl in wl_grid:
            self.spec_dens_Evans.append(
                expected_sig.spec_dens_Evans_for_plot(
                    temp_elec_ev, temp_ion_ev, wl, wl_laser, theta_deg, n_e_m, z_eff
                )
            )
            spec_dens_Selden.append(
                expected_sig.spect_dens_Selden(temp_elec_ev, wl, theta_deg, wl_laser)
            )

        salpeter = self.SolpiterSpinBox.value()

        pl = graphs.plot_section(
            wl_grid, self.spec_dens_Evans, spec_dens_Selden, wl_laser
        )

        toolbar = NavigationToolbar(pl, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(pl)
        self.widget_for_plot.setLayout(layout)
        layout.deleteLater()

        alpha_1 = 1 + salpeter**2
        self.SpecDens_theor.setValue(
            1 / alpha_1
            + z_eff
            * salpeter**4
            / (alpha_1 * (alpha_1 + z_eff * salpeter**2 * temp_elec_ev / temp_ion_ev))
        )
        self.SpecDenSel_calc.setValue(sum(spec_dens_Selden) * wl_step)
        self.SpecDenEv_calc.setValue(sum(self.spec_dens_Evans) * wl_step)

        self.PhEldata_label_2.setStyleSheet("background-color: rgb(70, 200, 100);")
        self.PhEldata_label_2.setText("Ready")

    def Load_filter_data(self):
        filter_path = self.FilterlineEdit.text()

        if not os.path.exists(filter_path):
            self.filter_status_label.setText("File was not found ")
            self.filter_status_label.setStyleSheet(
                "background-color:   rgb(255, 64, 99);"
            )

            self.f_data_wl = None
            self.f_data_trans = None
            self.num_of_filters = None

            self.Filter_Origdata_label.setText("no data")
            self.Filter_Origdata_label.setStyleSheet(
                "background-color:   rgb(255, 64, 99);"
            )

            self.SpecChdata_label.setText("no data")
            self.SpecChdata_label.setStyleSheet("background-color:   rgb(255, 64, 99);")

            self.poly_ind[1] = False
            self.PolyData_label.setStyleSheet("background-color:   rgb(255, 64, 99);")
            self.PolyData_label.setText("no data")

            return 0

        self.f_data_wl, self.f_data_trans, self.num_of_filters = (
            expected_sig.load_filter_data(filter_path)
        )

        self.filter_status_label.setText(
            "Filters data was loaded, number of filters:%d" % self.num_of_filters
        )
        self.filter_status_label.setStyleSheet("background-color: rgb(114, 255, 142);")

        self.Filter_Origdata_label.setText("Ready")
        self.Filter_Origdata_label.setStyleSheet("background-color: rgb(70, 200, 100);")

        self.SpecChdata_label.setText("Ready")
        self.SpecChdata_label.setStyleSheet("background-color: rgb(70, 200, 100);")

        self.poly_ind[0] = True

        if self.poly_ind[0] and self.poly_ind[1] and self.poly_ind[2]:
            self.PolyData_label.setText("Ready")
            self.PolyData_label.setStyleSheet("background-color: rgb(70, 200, 100);")

        return 1

    def Show_orig_filters(self):
        if self.num_of_filters is None:
            self.Filter_Origdata_label.setStyleSheet(
                "background-color: rgb(255, 94, 105);"
            )
            return 0
        else:
            self.Filter_Origdata_label.setStyleSheet(
                "background-color:  rgb(88, 255, 51);"
            )
            self.Filter_Origdata_label.setText("Was watched")
            pl = graphs.plot_orig_filters(
                self.f_data_wl, self.f_data_trans, self.num_of_filters
            )
            toolbar = NavigationToolbar(pl, self)

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(pl)

            self.widget_for_plot.setLayout(layout)
            layout.deleteLater()
            return 1

    def Build_Show_spec_ch(self):
        if self.num_of_filters is None:
            self.SpecChdata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
            return 0

        else:

            wl_start = self.wlStartSpinBox.value()
            num_of_steps = int(self.WlStepsSpinBox.value())
            wl_step = (self.wlEndSpinBox.value() - wl_start) / num_of_steps

            wl_grid = [wl_start + wl_step * i for i in range(num_of_steps)]

            self.spec_ch_data = expected_sig.build_spec_channels(
                wl_grid, self.f_data_wl, self.f_data_trans
            )

            layout = QtWidgets.QVBoxLayout()
            pl = graphs.plot_spec_ch(wl_grid, self.spec_ch_data, self.num_of_filters)
            toolbar = NavigationToolbar(pl, self)
            layout.addWidget(toolbar)
            layout.addWidget(pl)

            self.widget_for_plot.setLayout(layout)
            layout.deleteLater()

            self.poly_ind[1] = True

            if self.poly_ind[0] and self.poly_ind[1] and self.poly_ind[2]:
                self.PolyData_label.setText("Ready")
                self.PolyData_label.setStyleSheet(
                    "background-color: rgb(70, 200, 100);"
                )

            self.SpecChdata_label.setStyleSheet("background-color:  rgb(88, 255, 51);")
            self.SpecChdata_label.setText("Was watched")

    def Load_detector_data(self):

        detector_path = self.DetectorPathlineEdit.text()
        if not os.path.exists(detector_path):
            self.Detectordata_label.setText("File was not found")
            self.Detectordata_label.setStyleSheet(
                "background-color:   rgb(255, 64, 99);"
            )

            self.DetectorShowData_label.setText("no data")
            self.DetectorShowData_label.setStyleSheet(
                "background-color:  rgb(255, 64, 99);"
            )

            self.detector_wl = None
            self.detector_data = None

            return 0
        else:
            self.detector_wl, self.detector_data = expected_sig.load_detector_data(
                detector_path
            )
            self.Detectordata_label.setText("Detector data was loaded")
            self.Detectordata_label.setStyleSheet(
                "background-color: rgb(114, 255, 142);"
            )

            self.DetectorShowData_label.setText("Ready")
            self.DetectorShowData_label.setStyleSheet(
                "background-color: rgb(70, 200, 100);"
            )

            self.poly_ind[2] = True

            if self.poly_ind[2] and self.poly_ind[1]:
                self.poly_ind[2] = True
                self.PolyData_label.setText("Ready")
                self.PolyData_label.setStyleSheet(
                    "background-color: rgb(70, 200, 100);"
                )

    def Show_detector_data(self):
        if self.detector_wl is None:
            return 0
        else:
            self.DetectorShowData_label.setStyleSheet(
                "background-color:  rgb(88, 255, 51);"
            )
            self.DetectorShowData_label.setText("Was watched")

            pl = graphs.plot_detector_data(self.detector_wl, self.detector_data)
            toolbar = NavigationToolbar(pl, self)
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(pl)
            self.widget_for_plot.setLayout(layout)
            layout.deleteLater()

    def Build_Show_poly(self):

        if self.spec_ch_data is None or self.detector_data is None:
            self.PolyData_label.setText(
                "Build spectral channels and load detector data first"
            )
            return 0
        else:
            wl_laser = self.LWSpinBox.value()
            wl_start = self.wlStartSpinBox.value()
            num_of_steps = int(self.WlStepsSpinBox.value())
            wl_step = (self.wlEndSpinBox.value() - wl_start) / num_of_steps

            wl_grid = [wl_start + wl_step * i for i in range(num_of_steps)]

            self.poly_channels = expected_sig.build_poly(
                wl_grid, self.spec_ch_data, self.detector_wl, self.detector_data
            )

            layout = QtWidgets.QVBoxLayout()
            pl = graphs.plot_poly_data(wl_grid, self.poly_channels, wl_laser)
            toolbar = NavigationToolbar(pl, self)
            layout.addWidget(toolbar)
            layout.addWidget(pl)

            self.widget_for_plot.setLayout(layout)
            layout.deleteLater()

            self.PolyData_label.setText("Was watched")
            self.PolyData_label.setStyleSheet("background-color:  rgb(88, 255, 51);")

            self.PhEldata_label.setText("Ready")
            self.PhEldata_label.setStyleSheet("background-color: rgb(70, 200, 100);")

    def Calculate_phel(self):
        if self.poly_channels is None:
            self.PhEldata_label.setText("Build poly first")
            return 0
        else:
            n_e_m = self.ConcSpinBox.value() * 1e19

            theta_deg = self.ThetaSpinBox.value()
            solid_angle = self.OmegaSpinBox.value()
            z_eff = self.ZeffSpinBox.value()
            scattering_len = self.ScatLenSpinBox.value()

            laser_energy = self.LEnSpinBox.value()
            wl_laser = self.LWSpinBox.value()
            optic_trans = self.OpticTranslabel.value()

            ph_energy = (
                all_const["h_plank"] * all_const["c_light"] * 1e-2 / (wl_laser * 1e-9)
            )
            w_to_lambda = (
                2 * math.pi * all_const["c_light"] * 1e-2
            )  # /lambda in integral

            self.const = (
                scattering_len
                * solid_angle
                * n_e_m
                * laser_energy
                * optic_trans
                * w_to_lambda
                / ph_energy
            )
            self.const = (
                self.const * 1e9
            )  # 1E-9 from wl_step and (1E-18)^(-1) from lambda^-2

            wl_start = self.wlStartSpinBox.value()
            num_of_steps = int(self.WlStepsSpinBox.value())
            wl_step = (self.wlEndSpinBox.value() - wl_start) / num_of_steps

            wl_grid = [wl_start + wl_step * i for i in range(num_of_steps)]

            Te_start = self.TempStartSpinBox.value()
            Te_num_of_steps = int(self.TempStepsSpinBox.value())
            Te_step = (self.TempEndSpinBox.value() - Te_start) / Te_num_of_steps

            Te_grid = [Te_start + Te_step * i for i in range(Te_num_of_steps)]

            results = []
            sigma = []

            for T in Te_grid:
                sigma_from_T = []
                for wl in wl_grid:
                    sigma_from_T.append(
                        expected_sig.section_Evans(
                            T, T, wl, wl_laser, theta_deg, n_e_m, z_eff
                        )
                    )
                    self.PhEldata_label.setText("T = %f eV,\n wl = %f nm" % (T, wl))
                    QtWidgets.QApplication.processEvents()
                sigma.append(sigma_from_T)

            for channel in range(self.num_of_filters):
                ch_phel = []
                for j in range(len(Te_grid)):
                    integral = 0
                    for i in range(len(wl_grid)):
                        integral = integral + sigma[j][i] * self.poly_channels[channel][
                            i
                        ] / (wl_grid[i] ** 2)
                    ch_phel.append(integral * self.const * wl_step)
                results.append(ch_phel)

            layout = QtWidgets.QVBoxLayout()
            pl = graphs.plot_phel(Te_grid, results)
            toolbar = NavigationToolbar(pl, self)
            layout.addWidget(toolbar)
            layout.addWidget(pl)

            for i in range(len(Te_grid)):
                print(Te_grid[i], results[0][i], results[1][i])

            self.widget_for_plot.setLayout(layout)
            layout.deleteLater()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
