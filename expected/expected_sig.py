import json
import phys_const as const
import math

with open(
    "D:\Ioffe\TS\divertor_thomson\different_calcuations_py\spectre_for_low_T\expected\constants",
    "r",
) as file:
    all_const = json.load(file)
    file.close()


def Gamma(alpha: float, x: float) -> float:
    # необходима для расчета сечения
    t_steps_number = int(2e3)
    step_t = abs(x / t_steps_number)
    t_grid = [0 + i * step_t for i in range(t_steps_number)]
    exp_grid = [math.exp((t_grid[i]) ** 2 - x**2) for i in range(len(t_grid))]
    integral = step_t * sum(exp_grid)
    if x < 0:
        integral = integral * (-1)

    gamma = math.exp(-(x**2)) / (
        (1 - alpha**2 * (2 * x * integral - 1)) ** 2
        + math.pi * alpha**4 * x**2 * math.exp(-2 * x**2)
    )

    return gamma


def spec_dens_Evans_for_plot(
    temp_elec_ev: float,
    temp_ions_ev: float,
    wavelen_scat_nm: float,
    wavelen_incident_nm: float,
    theta_deg: float,
    n_e_m: float,
    z_eff: float,
) -> float:
    #                                               !!!!!CГС!!!!
    # спектр взят с Пятницкого стр 165. (6.2) - у него из Эванса
    #  отличается от section_Evans только тем, что сечение домножается на частоту, на которой ищется

    n_e_cm = n_e_m / 1e6
    wavelen_scat = wavelen_scat_nm * 1e-7  # centimeters
    wavelen_incident = wavelen_incident_nm * 1e-7  # centimeters

    omega = 2 * math.pi * all_const["c_light"] / wavelen_scat
    omega_0 = 2 * math.pi * all_const["c_light"] / wavelen_incident
    # print('omega %.4e' %omega)

    theta_rad = theta_deg * math.pi / 180

    # Solpeter alpha = 1/(K * Debay), k =  2 * omega * sin(a/2) (пятницкий, стр 54 (2.60) ) , omega = 2 * pi * c / nu

    debay = (
        temp_elec_ev
        * all_const["ev_to_erg"]
        / (4 * math.pi * n_e_cm * all_const["q_e"] ** 2)
    ) ** (
        1 / 2
    )  # centimeters
    # print('debay, cm', debay)

    alpha = all_const["c_light"] / (2 * omega * math.sin(theta_rad / 2) * debay)
    # print('solpeter', alpha)

    beta_squared = z_eff * (temp_elec_ev / temp_ions_ev) * (alpha**2 / (1 + alpha**2))

    beta = beta_squared**0.5

    omega_e = (
        2
        * omega
        * (2 * temp_elec_ev * all_const["ev_to_erg"] / all_const["m_e"]) ** 0.5
        * math.sin(theta_rad / 2)
        / all_const["c_light"]
    )
    omega_i = (
        2
        * omega
        * (2 * temp_ions_ev * all_const["ev_to_erg"] / all_const["m_ion"]) ** 0.5
        * math.sin(theta_rad / 2)
        / all_const["c_light"]
    )

    Omega = omega - omega_0

    x = Omega / omega_e
    y = Omega / omega_i
    w_to_lambda = 2 * math.pi * all_const["c_light"] * 1e-8  # /lambda in integral

    # const = all_const['q_e'] ** 4 / (all_const['m_e'] ** 2 * all_const['c_light'] ** 4 * math.pi ** (1 / 2)) * 1E-4  # 1E-4 - to meters^2
    sigma = (
        (
            Gamma(alpha, x) / omega_e
            + z_eff * (alpha**2 / (1 + alpha**2)) ** 2 * Gamma(beta, y) / omega_i
        )
        * omega
        * (omega / omega_0) ** 2
        / w_to_lambda
    )

    return sigma


def section_Evans(
    temp_elec_ev: float,
    temp_ions_ev: float,
    wavelen_scat_nm: float,
    wavelen_incident_nm: float,
    theta_deg: float,
    n_e_m: float,
    z_eff: float,
) -> float:
    #                                               !!!!!CГС!!!!
    # спектр взят с Пятницкого стр 165. (6.2) - у него из Эванса
    with open(
        "D:\Ioffe\TS\divertor_thomson\different_calcuations_py\spectre_for_low_T\expected\constants",
        "r",
    ) as file:
        all_const = json.load(file)

    n_e_cm = n_e_m / 1e6
    wavelen_scat = wavelen_scat_nm * 1e-7  # centimeters
    wavelen_incident = wavelen_incident_nm * 1e-7  # centimeters

    omega = 2 * math.pi * all_const["c_light"] / wavelen_scat
    omega_0 = 2 * math.pi * all_const["c_light"] / wavelen_incident
    # print('omega %.4e' %omega)

    theta_rad = theta_deg * math.pi / 180

    # Solpeter alpha = 1/(K * Debay), k =  2 * omega * sin(a/2) (пятницкий, стр 54 (2.60) ) , omega = 2 * pi * c / nu

    debay = (
        temp_elec_ev
        * all_const["ev_to_erg"]
        / (4 * math.pi * n_e_cm * all_const["q_e"] ** 2)
    ) ** (
        1 / 2
    )  # centimeters
    # print('debay, cm', debay)

    alpha = all_const["c_light"] / (2 * omega * math.sin(theta_rad / 2) * debay)
    # print('solpeter', alpha)

    beta_squared = z_eff * (temp_elec_ev / temp_ions_ev) * (alpha**2 / (1 + alpha**2))

    beta = beta_squared ** (1 / 2)

    omega_e = (
        2
        * omega
        * (2 * temp_elec_ev * all_const["ev_to_erg"] / all_const["m_e"]) ** (1 / 2)
        * math.sin(theta_rad / 2)
        / all_const["c_light"]
    )
    omega_i = (
        2
        * omega
        * (2 * temp_ions_ev * all_const["ev_to_erg"] / all_const["m_ion"]) ** (1 / 2)
        * math.sin(theta_rad / 2)
        / all_const["c_light"]
    )

    Omega = omega - omega_0

    x = Omega / omega_e
    y = Omega / omega_i

    const = (
        all_const["q_e"] ** 4
        / (all_const["m_e"] ** 2 * all_const["c_light"] ** 4 * math.pi ** (1 / 2))
        * 1e-4
    )  # 1E-4 - to meters^2

    # ions_input_cons = (temp_elec_ev * all_const['m_ion'] / (temp_ions_ev * all_const['m_e']) )**0.5

    sigma = const * (
        Gamma(alpha, x) / omega_e
        + z_eff * (alpha**2 / (1 + alpha**2)) ** 2 * Gamma(beta, y) / omega_i
    )

    return sigma  # m^2/ ( st * s)


def spect_dens_Selden(
    temp: float, wl: float, theta_deg: float, lambda_0: float
) -> float:
    alphaT = const.m_e * const.c * const.c / (2 * const.q_e)
    theta = theta_deg * math.pi / 180.0

    alpha = alphaT / temp
    x = (wl / lambda_0) - 1
    a_loc = math.pow(1 + x, 3) * math.sqrt(
        2 * (1 - math.cos(theta)) * (1 + x) + math.pow(x, 2)
    )
    b_loc = math.sqrt(1 + x * x / (2 * (1 - math.cos(theta)) * (1 + x))) - 1
    c_loc = math.sqrt(alpha / math.pi) * (
        1 - (15 / 16) / alpha + 345 / (512 * alpha * alpha)
    )
    return (c_loc / a_loc) * math.exp(-2 * alpha * b_loc) / lambda_0


def load_filter_data(filter_path: str) -> object:
    # возвращает 2 списка списков. 1 - длины волн, 2 - пропускание.
    # требует на вход файл, в котором каждому фильтру соответствует 2 столбца - длина волны и пропускание.
    # 3 фильтра - 3 пары(6 столбцов)

    with open(filter_path, "r") as file:
        filters_data = file.readlines()

    filters_data_wl = []
    filters_data_trans = []

    for j in range(int(len(filters_data[2].split(",")) / 2)):
        temp_wl = []
        temp_trans = []

        for i in range(2, len(filters_data)):
            if float(filters_data[i].split(",")[2 * j + 1]) < 0:
                temp_wl.append(float(filters_data[i].split(",")[2 * j]))
                temp_trans.append(0)
            else:
                try:
                    temp_wl.append(float(filters_data[i].split(",")[2 * j]))
                    temp_trans.append(float(filters_data[i].split(",")[2 * j + 1]))

                except ValueError:

                    temp_wl.append(temp_wl[i - 2] + 10)
                    temp_trans.append(0)

        if temp_wl[0] > temp_wl[1]:
            temp_wl.reverse()
            temp_trans.reverse()

        filters_data_wl.append(temp_wl)
        filters_data_trans.append(temp_trans)

    print("Filters data loaded, number of filters:", len(filters_data_trans))

    return filters_data_wl, filters_data_trans, len(filters_data_trans)


def load_detector_data(detector_path: str) -> (list, list):
    # реверс в конце функции - начальная характеристика дана с 1100nm -> 600nm
    with open(detector_path, "r") as file:
        detector_file = file.readlines()

    detector_wl = []
    detector_phel = []

    for i in range(2, len(detector_file)):
        detector_wl.append(float(detector_file[i].split(",")[0]))
        detector_phel.append(
            float(detector_file[i].split(",")[1]) / 100
        )  # данные в файле - в процентах, поэтому /100 !

    print("Detector data loaded")

    detector_wl.reverse()
    detector_phel.reverse()

    return detector_wl, detector_phel


def load_detector_aw(detector_path: str) -> (list, list):
    """
    :param avalanche_path:
    :return: 2 списка: длину волны в нм и квантовый выход phe/photon
    """
    h_plank = 6.63e-34
    c = 3e8
    e_charge = 1.602e-19

    full_coef = h_plank * c * 1e9 / e_charge  # 10E9 переход к метрам

    with open(detector_path) as avalanche_data:
        aval_wl = []
        aval_aw = []
        for line in avalanche_data.readlines():
            if any(sym.isalpha() for sym in line):
                pass
            else:
                line = line[:-2]
                wl, aw = line.split(",")
                aval_wl.append(float(wl))
                aval_aw.append(float(aw))
        aval_phe = [aw * full_coef / wl for aw, wl in zip(aval_aw, aval_wl)]

    return aval_wl, aval_phe


def build_spec_channels(wl_grid: list, filters_wl: list, filters_trans: list) -> list:
    # спектральная характеристика каналов на сетке по длине волны
    all_ch_trans = []
    all_ch_reflect = []
    all_trans_original = []
    for ch_num in range(len(filters_trans)):
        ch_trans = []
        ch_reflect = []

        trans_original = []
        for wl_ind in range(len(wl_grid)):

            if (
                wl_grid[wl_ind] < filters_wl[ch_num][0]
                or wl_grid[wl_ind] > filters_wl[ch_num][-1]
            ):
                trans = 0
                reflect = 1
            else:
                filter_ind = 0
                while filters_wl[ch_num][filter_ind] < wl_grid[wl_ind]:
                    filter_ind = filter_ind + 1

                trans = filters_trans[ch_num][filter_ind - 1] + (
                    filters_trans[ch_num][filter_ind]
                    - filters_trans[ch_num][filter_ind - 1]
                ) / (
                    filters_wl[ch_num][filter_ind] - filters_wl[ch_num][filter_ind - 1]
                ) * (
                    wl_grid[wl_ind] - filters_wl[ch_num][filter_ind - 1]
                )

                trans_original.append(trans)
                if ch_num == 0:
                    reflect = 1 - trans
                else:
                    trans = trans * all_ch_reflect[ch_num - 1][wl_ind]
                    reflect = all_ch_reflect[ch_num - 1][wl_ind] - trans

            ch_trans.append(trans)
            ch_reflect.append(reflect)

        all_ch_trans.append(ch_trans)
        all_ch_reflect.append(ch_reflect)
        all_trans_original.append(trans_original)

    #
    # with open('tmp.json', 'w') as file:
    #     json.dump({
    #         'filter': all_trans_original,
    #         't': all_ch_trans,
    #         'r': all_ch_reflect,
    #         'w': wl_grid
    #     }, file)

    return all_ch_trans


def build_poly(
    wl_grid: list, all_ch_trans: list, detector_wl: list, detector_phel: list
):
    # multiply spectral data by approx on grid detector data
    channels = []
    for ch_num in range(len(all_ch_trans)):
        temp_ch = []
        for wl_ind in range(len(wl_grid)):
            filter_ind = 0
            while wl_grid[wl_ind] > detector_wl[filter_ind]:
                filter_ind = filter_ind + 1

            detector = detector_phel[filter_ind] + (
                detector_phel[filter_ind + 1] - detector_phel[filter_ind]
            ) / (detector_wl[filter_ind + 1] - detector_wl[filter_ind]) * (
                wl_grid[wl_ind] - detector_wl[filter_ind]
            )
            # линейная интерполяция
            temp_ch.append(all_ch_trans[ch_num][wl_ind] * detector)

            # all_ch_trans[ch_num][wl_ind] = all_ch_trans[ch_num][wl_ind] * detector * 0.97**ch_num
        channels.append(temp_ch)
    return channels


if __name__ == "__main__":
    print("tut expected sig main")
    with open(
        "D:\Ioffe\TS\divertor_thomson\different_calcuations_py\spectre_for_low_T\expected\constants",
        "r",
    ) as file:
        all_const = json.load(file)
        file.close()

    laser_energy = 2  # J
    scattering_len = 17e-3  # m
    optic_trans = 0.2  # path to poly
    T_i = 100  # ev
    laser_len = 1064.4  # nm
    theta_scat = 110
    zeff = 2
    omega_scat = 0.0025

    ph_energy = all_const["h_plank"] * all_const["c_light"] * 1e-2 / (laser_len * 1e-9)
    w_to_lambda = 2 * math.pi * all_const["c_light"] * 1e-2  # /lambda in integral
    power = 1e9  # 1E-9 from wl_step and (1E-18)^(-1) from lambda^-2

    start_wl = 900  # nm
    finish_wl = 1070  # nm
    steps_number = 2000
    wl_step = (finish_wl - start_wl) / steps_number
    wl_grid_nm = [start_wl + i * wl_step for i in range(steps_number)]

    detector_wl, detector_data = load_detector_aw("aw.csv")

    filters_data_wl, filters_data_trans, chan_num = load_filter_data(
        "filters_equator.csv"
    )

    all_ch_trans = build_spec_channels(wl_grid_nm, filters_data_wl, filters_data_trans)
    build_poly(wl_grid_nm, all_ch_trans, detector_wl, detector_data)

    for i in range(len(all_ch_trans[0])):
        break
        print(wl_grid_nm[i], all_ch_trans[0][i], all_ch_trans[1][i])

    for i in range(len(filters_data_trans[0])):
        break
        print(
            filters_data_wl[0][i],
            filters_data_trans[0][i],
            filters_data_wl[1][i],
            filters_data_trans[1][i],
        )

    for wl in wl_grid_nm:
        break
        # section_Evans(0.3, 0.3, wl, 1064.4, 110, 1E22, 2)
        print("%.5e %.4e " % (wl, section_Evans(50, 50, wl, 1064.4, 135, 1e20, zeff)))

    T_e = [0.1 + i * 0.1 for i in range(150)]  # ev
    n_e = 1e20
    for wl in wl_grid_nm:
        break
        print(
            "%.5e %.4e " % (wl, section_Evans(0.3, 0.3, wl, 1064.4, 130, 1e21, zeff))
        )  # sigma / (omega_frequency * omega_scat) или же сечение на такой частоте в такой телесный угол) m^2 * s / st
        # print(' %.4e ' % (section_Evans(0.3, 0.3, wl, 1064.4, 130, 1E21, zeff)))

    results = []
    const = (
        scattering_len
        * omega_scat
        * n_e
        * laser_energy
        * optic_trans
        * w_to_lambda
        / (ph_energy)
    )
    const = const * power

    for channel in range(chan_num):
        ch_phel = []
        for T in T_e:
            integral = 0
            for i in range(len(wl_grid_nm)):
                sigma = section_Evans(
                    T, T, wl_grid_nm[i], laser_len, theta_scat, n_e, zeff
                )  # m^2/ ( st * s)
                integral = integral + sigma * all_ch_trans[channel][i] / (
                    wl_grid_nm[i] ** 2
                )
            ch_phel.append(integral * const * wl_step)
        results.append(ch_phel)

    for i in range(len(T_e)):
        print(T_e[i], results[0][i], results[1][i])
