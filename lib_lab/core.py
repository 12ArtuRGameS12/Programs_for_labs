# from typing import Any, Callable
from .tools import *
from .primary_calculations import *


def prim_izmer(
        data: tuple[int | float, ...] | list[int | float],
        accuracy: int | float,
        interval: int = 2,
        debug: bool = False) -> tuple[float, float] | dict[str, float]:
    """
    Прямые измерения

    slp - случайная погрешность\n
    prp - приборная погрешность\n
    obp - абсолютная погрешность\n

    :param data: данные
    :param accuracy: точность прибора
    :param interval: доверительная вероятность(1=90%, 2=95%, 3=99%)
    :param debug: режим разработчика
    :return: средние значение и абсолютная погрешность
    """

    typetest((data,), (tuple, list), {0: "data"})
    typetest(data, (int, float))
    typetest((accuracy,), (int, float), {0: "accuracy"})
    typetest((debug,), (bool,), {0: "debug"})

    izmer: dict[str, int | float] = dict()
    x = stat(data)
    izmer["slp"] = stu(x["nX"] - 1, interval) * x["s0X"]
    izmer["prp"] = stu(9999, interval) * accuracy / 3
    izmer["obp"] = (izmer["slp"] ** 2 + izmer["prp"] ** 2) ** (1 / 2)

    if debug:
        return izmer
    else:
        return x["srX"], izmer["obp"]


def nerav_izmer(
        data: tuple[int | float, ...] | list[int | float],
        errors: tuple[int | float, ...] | list[int | float],
        debug: bool = False) -> tuple[float, float] | dict[str, int | float | list]:
    """Неравноточные измерения

    :param data: значения
    :param errors: погрешности
    :param debug: режим разработчика
    :return: средние значение и абсолютная погрешность
    """

    typetest((data, errors), (tuple, list), {0: "data", 1: "errors"})
    typetest(data, (int, float))
    typetest(errors, (int, float))
    typetest((debug,), (bool,), {0: "debug"})

    izmer: dict[str, int | float | list] = dict()
    izmer["w"] = list(map(lambda x: 1 / x ** 2, errors))
    izmer["x0"] = list(map(lambda x, y: x * y, izmer["w"], data))
    izmer["sum_x0"] = sum(izmer["x0"])
    izmer["sum_w"] = sum(izmer["w"])
    izmer["value"] = izmer["sum_x0"] / izmer["sum_w"]
    izmer["data_len"] = len(data)
    izmer["err"] = (izmer["data_len"] / izmer["sum_w"]) ** (1 / 2)
    if debug:
        return izmer
    else:
        return izmer["value"], izmer["err"]


def mnc(
        arg1: tuple[int | float, ...] | list[int | float],
        arg2: tuple[int | float, ...] | list[int | float],
        interval: int = 2,
        mode: int = 1,
        debug: bool = False) -> (
        (tuple[float, tuple[float, float], tuple[float, float]] |
         tuple[float, tuple[float, float]]
         ) | dict[str, int | float | list]):
    """Метод наименьших квадратов

    :param arg1: значения x
    :param arg2: значения y
    :param mode: 1: y = ax + b, 2: y = ax
    :param interval: доверительная вероятность(1=90%, 2=95%, 3=99%
    :param debug: режим разработчика
    :return: R, (a, da), (b, db)
    """

    typetest((arg1, arg2), (tuple, list), {0: "arg1", 1: "arg2"})
    typetest(arg1, (int, float))
    typetest(arg2, (int, float))
    if mode not in (1, 2):
        raise ValueError(f"Нету такой формулы {mode}")
    typetest((debug,), (bool,), {0: "debug"})

    stt1 = stat(arg1, arg2)
    mncc1: dict[str, int | float | list] = dict()

    if mode == 1:
        if (len(arg1) < 3) or (len(arg2) < 3):
            raise ValueError("Меньше трёх нельзя в режиме 1")

        mncc1["a0"] = (stt1["nX"] * stt1["sumXY"] - stt1["sumX"] * stt1["sumY"]) / (
                stt1["nX"] * stt1["sumX2"] - stt1["sumX"] ** 2)
        mncc1["b0"] = (stt1["sumX2"] * stt1["sumY"] - stt1["sumX"] * stt1["sumXY"]) / (
                stt1["nX"] * stt1["sumX2"] - stt1["sumX"] ** 2)
        mncc1["r0"] = (stt1["sumXXYY"]) / ((stt1["sumXX2"] ** (1 / 2)) * (stt1["sumYY2"] ** (1 / 2)))
        mncc1["q"] = list(map(lambda x, y: (mncc1["a0"] * x + mncc1["b0"] - y) ** 2, arg1, arg2))
        mncc1["sum_q"] = sum(mncc1["q"])
        mncc1["sa"] = (mncc1["sum_q"] / ((stt1["nX"] - 2) * stt1["sumXX2"])) ** (1 / 2)
        mncc1["sb"] = (mncc1["sum_q"] / stt1["nX"] / (stt1["nX"] - 2) + stt1["srX"] ** 2 * mncc1["sa"]) ** (1 / 2)
        mncc1["da"] = stu(stt1["nX"] - 2, interval) * mncc1["sa"]
        mncc1["db"] = stu(stt1["nX"] - 2, interval) * mncc1["sb"]
    else:
        mncc1["r0"] = (stt1["sumXXYY"]) / ((stt1["sumXX2"] ** (1 / 2)) * (stt1["sumYY2"] ** (1 / 2)))
        mncc1["a0"] = stt1["sumXY"] / stt1["sumX2"]
        mncc1["q"] = list(map(lambda x, y: (mncc1["a0"] * x - y) ** 2, arg1, arg2))
        mncc1["sum_q"] = sum(mncc1["q"])
        mncc1["sa"] = (mncc1["sum_q"] / ((stt1["nX"] - 1) * stt1["sumXX2"])) ** (1 / 2)
        mncc1["da"] = stu(stt1["nX"] - 1, interval) * mncc1["sa"]

    if debug:
        return mncc1
    else:
        if mode == 1:
            return mncc1["r0"], (mncc1["a0"], mncc1["da"]), (mncc1["b0"], mncc1["db"])
        elif mode == 2:
            return mncc1["r0"], (mncc1["a0"], mncc1["da"])


def cosn_izmer_formula(formula: str, *varabels: str) -> str:
    """Дельта формулы при косвенных измерениях

    :param formula: формула
    :param varabels: значения, у которых есть погрешность
    :return: дельта формулы
    """

    typetest((formula, *varabels), (str,), {0: formula})

    import sympy
    x = sympy.sympify(0)
    for i in varabels:
        x += (sympy.diff(formula, i) * sympy.symbols(f"d{i}")) ** 2
    x = sympy.sqrt(x)
    return x.__str__()


def convert2number(num_str: str) -> int | float:
    """Конвертируя строку в число

    :param num_str: число в виде строки
    :return: число в виде int или float
    """

    typetest((num_str,), (str,), {0: "num_str"})

    try:
        x = int(num_str)
    except ValueError:
        x = float(num_str)

    return x


def formul_exe(
        formula: str,
        varabels: dict[str, int | float | str]) -> tuple[int, str] | tuple[float, str]:
    """Счёт значения формулы

    :param formula:
    :param varabels:
    :return: значение формулы
    """

    typetest((varabels,), (dict,), {0: "varabels"})
    typetest((formula, *varabels), (str,), {0: "formul"})
    typetest(([varabels[i] for i in varabels]), (int, float, str))

    import sympy
    formula = sympy.sympify(formula)
    formula = formula.subs(varabels)

    try:
        x = convert2number(formula.evalf().__str__())
    except ValueError:
        x = "err"
    return x, formula.__str__()
