from .tools import *


def stu(n: int, interval: int = 2) -> float:
    """Даёт значение Стьюдента

    :param n: число степеней свободы
    :param interval: доверительная вероятность(1=90%, 2=95%, 3=99%)
    :return: значение Стьюдента
    """

    typetest((n, interval), (int,), {0: "n", 1: "a"})

    if interval not in (1, 2, 3):
        raise ValueError(f"Нету в таблице такой доверительной вероятности как {interval}")

    table_students = {
        1: (6.314, 12.706, 63.619),
        2: (2.92, 4.303, 9.925),
        3: (2.353, 3.182, 5.841),
        4: (2.132, 2.776, 4.604),
        5: (2.015, 2.571, 4.032),
        6: (1.943, 2.447, 3.707),
        7: (1.895, 2.365, 3.499),
        8: (1.86, 2.306, 3.355),
        9: (1.833, 2.262, 3.25),
        10: (1.812, 2.228, 3.169),
        11: (1.796, 2.201, 3.106),
        12: (1.782, 2.179, 3.055),
        13: (1.771, 2.16, 3.012),
        14: (1.761, 2.145, 2.977),
        15: (1.753, 2.131, 2.947),
        16: (1.746, 2.12, 2.921),
        17: (1.74, 2.11, 2.898),
        18: (1.734, 2.103, 2.878),
        19: (1.729, 2.093, 2.861),
        20: (1.725, 2.086, 2.845),
        21: (1.721, 2.08, 2.831),
        22: (1.717, 2.074, 2.819),
        23: (1.714, 2.069, 2.807),
        24: (1.711, 2.064, 2.797),
        25: (1.708, 2.06, 2.787),
        26: (1.706, 2.056, 2.779),
        27: (1.703, 2.052, 2.771),
        28: (1.701, 2.048, 2.763),
        29: (1.699, 2.045, 2.756),
        30: (1.697, 2.042, 2.75),
        40: (1.684, 2.021, 2.704),
        60: (1.671, 2.0, 2.66),
        120: (1.658, 1.98, 2.617),
        9999: (1.645, 1.96, 2.576)
    }

    try:
        x = table_students[n][interval - 1]
    except KeyError:
        raise ValueError(f"Нету в таблице такой степени свободы как {n}")

    return x


def stat(
        arg1: tuple[int | float, ...] | list[int | float],
        arg2: tuple[int | float, ...] | list[int | float] = None) -> dict[str, int | float]:
    """Статистика значений

    nX = количество элементов \n

    sumX = сумма X \n
    srX = sumX / nX \n

    XX = Xi - srX \n
    sumXX = сумма (Xi - srX) \n

    XX2 = (Xi - srX) ** 2 \n
    sumXX2 = сумма (Xi - srX) ** 2 \n

    s0X = (sumXX2 / {nX * [nX - 1]}) ** (1/2) \n

    X2 = Xi ** 2 \n
    sumX2 = сумма Xi ** 2 \n

    XY = Xi * Yi \n
    sumXY = сумма Xi * Yi \n

    XXYY = (Xi - srX) * (Yi - srY) \n
    sumXXYY = сумма (Xi - srX) * (Yi - srY) \n

    :param arg1: список первой переменной
    :param arg2: список второй переменной
    :return: словарь данных
    """

    typetest((arg1,), (tuple, list), {0: "arg1"})
    typetest(arg1, (int, float))
    if len(arg1) <= 1:
        raise ValueError("Меньше двух нельзя")

    if arg2:
        typetest((arg2,), (tuple, list), {0: "arg2"})
        typetest(arg2, (int, float))
        arg1_len = len(arg1)
        arg2_len = len(arg2)
        if arg2_len <= 1:
            raise ValueError("Меньше двух нельзя")
        if arg1_len != arg2_len:
            raise ValueError(f"Длина arg1 - {arg1_len} != arg2 - {arg2_len}")

    def _stat1(arg: tuple[int | float, ...] | list[int | float],
               name: str) -> dict[str, int | float | list]:

        z: dict[str, int | float | list] = dict()
        z[f"n{name}"] = len(arg)
        z[f"sum{name}"] = sum(arg)
        z[f"sr{name}"] = z[f"sum{name}"] / z[f"n{name}"]
        z[f"{name}{name}"] = list(map(lambda x: x - z[f"sr{name}"], arg), )
        z[f"sum{name}{name}"] = sum(z[f"{name}{name}"])
        z[f"{name}{name}2"] = list(map(lambda x: (x - z[f"sr{name}"]) ** 2, arg), )
        z[f"sum{name}{name}2"] = sum(z[f"{name}{name}2"])
        z[f"s0{name}"] = (z[f"sum{name}{name}2"] / (z[f"n{name}"] * (z[f"n{name}"] - 1))) ** (1 / 2)
        z[f"{name}2"] = list(map(lambda x: x ** 2, arg))
        z[f"sum{name}2"] = sum(z[f"{name}2"])
        return z

    if not arg2:
        return _stat1(arg1, "X")
    else:
        stt = _stat1(arg1, "X") | _stat1(arg2, "Y")
        stt["XY"] = list(map(lambda x, y: x * y, arg1, arg2))
        stt["sumXY"] = sum(stt["XY"])
        stt["XXYY"] = list(map(lambda x, y: x * y, stt["XX"], stt["YY"]))
        stt["sumXXYY"] = sum(stt["XXYY"])
        return stt
