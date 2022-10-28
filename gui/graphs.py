import matplotlib as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
plt.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.axes.grid()


def plot_orig_filters(f_data_wl: list, f_data_trans: list, filter_num: int):
    sc = MplCanvas(width=11, height=5, dpi=100)
    for i in range(filter_num):
        sc.axes.plot(f_data_wl[i], f_data_trans[i])
    return sc


def plot_spec_ch(wl_grid: list, all_ch_trans: list,  filter_num: int):
    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.set_title('Spectral channels in poly ')
    sc.axes.set_ylabel('Trans ')
    for i in range(filter_num):
        sc.axes.plot(wl_grid, all_ch_trans[i])
    return sc


def plot_detector_data(detector_wl: list, detector_data: list):
    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.set_title('Detector data')
    sc.axes.set_ylabel('electrons per photon ')
    sc.axes.plot(detector_wl, detector_data)
    return sc


def plot_poly_data(wl_grid: list, all_ch_data: list):
    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.set_title('Poly\'s channels' )
    sc.axes.set_ylabel('Transp * electrons per photon ')
    for i in range(len(all_ch_data)):
        sc.axes.plot(wl_grid, all_ch_data[i])
    return sc


def plot_section(wl_grid: list, section: list):
    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.set_title('Thomson scattering section at this wavelength to a given solid angle' )
    sc.axes.set_ylabel('sigma, m^2')
    sc.axes.plot(wl_grid, section)
    return sc
