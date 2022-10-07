import matplotlib as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
plt.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def plot_orig_filters(f_data_wl: list, f_data_trans: list, filter_num: int):
    sc = MplCanvas(width=10, height=4, dpi=100)
    for i in range(filter_num):
        sc.axes.plot(f_data_wl[i], f_data_trans[i])
    return sc


def plot_spec_ch(wl_grid: list, all_ch_trans: list,  filter_num: int):
    sc = MplCanvas(width=10, height=4, dpi=100)
    for i in range(filter_num):
        sc.axes.plot(wl_grid, all_ch_trans[i])
    return sc


def plot_detector_data(detector_wl: list, detector_data: list):
    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.plot(detector_wl, detector_data)

    return sc

