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


def plot_spec_ch(wl_grid: list, all_ch_trans: list, filter_num: int):
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


def plot_poly_data(wl_grid: list, all_ch_data: list, laser_wl: float):
    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.set_title('Poly\'s channels')
    sc.axes.set_ylabel('Transp * electrons per photon ')
    for i in range(len(all_ch_data)):
        sc.axes.plot(wl_grid, all_ch_data[i])
    sc.axes.vlines(laser_wl, ymin=min(all_ch_data[0]), ymax=max(all_ch_data[0]),
                   color='r',
                   linestyle='--')
    return sc


def plot_section(wl_grid: list, section_Evans: list, section_Selden: list, laser_wl: float):

    sc = MplCanvas(width=10, height=4, dpi=100)
    sc.axes.set_title('Thomson scattering section at this wavelength to a given solid angle')
    sc.axes.set_ylabel('sigma')
    sc.axes.set_xlabel('wavelength, nm')

    #section_Evans = [x / max(section_Evans) for x in section_Evans]
    #section_Selden = [x / max(section_Selden) for x in section_Selden]

    sc.axes.plot(wl_grid, section_Evans, label = 'Evans')
    sc.axes.plot(wl_grid, section_Selden, label = 'Selden')
    sc.axes.legend()
    sc.axes.set_xlim(min(wl_grid), max(wl_grid))
    sc.axes.vlines(laser_wl, ymin=min(section_Evans), ymax=max(section_Evans),
                   color='r',
                   label='laser wl',
                   linestyle='--')

    return sc


def plot_phel(Te_grid:list, ph_el : list):
    sc = MplCanvas(width=10, height=4, dpi=100)
    for i in range(len(ph_el)):
        sc.axes.plot(Te_grid, ph_el[i])
    sc.axes.set_xscale('log')
    return sc

