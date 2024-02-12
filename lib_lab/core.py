# from typing import Any, Callable
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

    z: dict[str, int | float] = dict()
    x = stat(data)
    z["slp"] = stu(x["nX"] - 1, interval) * x["s0X"]
    z["prp"] = stu(9999, interval) * accuracy / 3
    z["obp"] = (z["slp"] ** 2 + z["prp"] ** 2) ** (1 / 2)

    if debug:
        return z
    else:
        return x["srX"], z["obp"]


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

    z: dict[str, int | float | list] = dict()
    z["w"] = list(map(lambda x: 1 / x ** 2, errors))
    z["wa"] = list(map(lambda x, y: x * y, data, z["w"]))
    z["sum_wa"] = sum(z["wa"])
    z["sum_w"] = sum(z["w"])
    z["value"] = z["sum_wa"] / z["sum_w"]
    z["data_len"] = len(data)
    z["err"] = (z["data_len"] / z["sum_w"]) ** (1 / 2)
    if debug:
        return z
    else:
        return z["value"], z["err"]


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
    :param interval: доверительная вероятность(1=90%, 2=95%, 3=99%)
    :param debug: режим разработчика
    :return: R, (a, da), (b, db)
    """

    typetest((arg1, arg2), (tuple, list), {0: "arg1", 1: "arg2"})
    typetest(arg1, (int, float))
    typetest(arg2, (int, float))
    if mode not in (1, 2):
        raise ValueError(f"Нету такой формулы {mode}")
    typetest((debug,), (bool,), {0: "debug"})

    st = stat(arg1, arg2)
    z: dict[str, int | float | list] = dict()

    if mode == 1:
        if (len(arg1) < 3) or (len(arg2) < 3):
            raise ValueError("Меньше трёх нельзя в режиме 1")

        z["a0"] = (st["nX"] * st["sumXY"] - st["sumX"] * st["sumY"]) / (
                st["nX"] * st["sumX2"] - st["sumX"] ** 2)
        z["b0"] = (st["sumX2"] * st["sumY"] - st["sumX"] * st["sumXY"]) / (
                st["nX"] * st["sumX2"] - st["sumX"] ** 2)

        z["r0"] = (st["sumXXYY"]) / (st["sumXX2"] ** (1 / 2) * st["sumYY2"] ** (1 / 2))
        z["q"] = list(map(lambda x, y: (z["a0"] * x + z["b0"] - y) ** 2, arg1, arg2))
        z["sum_q"] = sum(z["q"])
        z["sa"] = (z["sum_q"] / ((st["nX"] - 2) * st["sumXX2"])) ** (1 / 2)
        z["sb"] = (z["sum_q"] / st["nX"] / (st["nX"] - 2) + st["srX"] ** 2 * z["sa"] ** 2) ** (1 / 2)
        z["da"] = stu(st["nX"] - 2, interval) * z["sa"]
        z["db"] = stu(st["nX"] - 2, interval) * z["sb"]
    else:
        z["a0"] = st["sumXY"] / st["sumX2"]
        z["r0"] = (st["sumXXYY"]) / (st["sumXX2"] ** (1 / 2) * st["sumYY2"] ** (1 / 2))
        z["q"] = list(map(lambda x, y: (z["a0"] * x - y) ** 2, arg1, arg2))
        z["sum_q"] = sum(z["q"])
        z["sa"] = (z["sum_q"] / ((st["nX"] - 1) * st["sumXX2"])) ** (1 / 2)
        z["da"] = stu(st["nX"] - 1, interval) * z["sa"]

    if debug:
        return z
    else:
        if mode == 1:
            return z["r0"], (z["a0"], z["da"]), (z["b0"], z["db"])
        elif mode == 2:
            return z["r0"], (z["a0"], z["da"])


def cosn_izmer_formula(formula: str, *varabels: str) -> str:
    """Дельта формулы при косвенных измерениях

    :param formula: формула
    :param varabels: значения, у которых есть погрешность
    :return: дельта формулы
    """

    typetest((formula, *varabels), (str,), {0: "formula"})

    import sympy
    x = sympy.sympify(0)
    for i in varabels:
        x += (sympy.diff(formula, i) * sympy.symbols(f"d{i}")) ** 2
    x = sympy.sqrt(x)
    return x.__str__()


def formula_exe(
        formula: str,
        varabels: dict[str, int | float | str]) -> tuple[int, str] | tuple[float, str]:
    """Счёт значения формулы

    :param formula:
    :param varabels:
    :return: значение формулы
    """

    typetest((varabels,), (dict,), {0: "varabels"})
    typetest((formula, *varabels), (str,), {0: "formula"})
    typetest(([varabels[i] for i in varabels]), (int, float, str))

    import sympy
    formula = sympy.sympify(formula)
    formula = formula.subs(varabels)

    try:
        x = convert2number(formula.evalf().__str__())
    except ValueError:
        x = "err"
    return x, formula.__str__()
