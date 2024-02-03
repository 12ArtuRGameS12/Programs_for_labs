"""Библиотека для работы над лабораторными данными

Есть функции, которые используют стороннее библиотеки, такие как:
sympy, matplotlib
"""


# from typing import Any


def typetest(
        input_data: tuple | list,
        include: tuple[type, ...] | list[type],
        name: dict[int, ...] = None) -> bool:
    """Функция для проверки типа и вызова исключения

    :param input_data: значения в виде списка
    :param include: с какими типами сравнивать
    :param name: имена переменных для ошибок
    :return: True или исключение
    """

    if name is None:
        name = {i: i for i in range(len(input_data))}
    else:
        name = {i: i for i in range(len(input_data))} | name

    for i, q in zip(input_data, name):
        i_type = type(i)
        if i_type not in include:

            include_text = ""
            include_len = len(include)
            for j in enumerate(include):
                if j[0] != include_len - 1:
                    include_text += str(j[1])[8:-2] + " или "
                else:
                    include_text += str(j[1])[8:-2]
            raise TypeError(f"{name[q]} - {str(i_type)[8:-2]} не {include_text}")

    return True


def clr_sp(text: str) -> str:
    """Чистит водимую строку от лишних пробелов"""

    typetest((text,), (str,), {0: "text"})

    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    while text.find(" ,") != -1:
        text = text.replace(" ,", ",")
    while text.find(", ") != -1:
        text = text.replace(", ", ",")
    if text[0] == " ":
        text = text[1:]
    if text[-1] == " ":
        text = text[:-1]

    return text


def stu(n: int, a: int = 2) -> float:
    """Даёт значение Стьюдента

    :param n: число степеней свободы
    :param a: доверительная вероятность(1=90%, 2=95%, 3=99%)
    :return: значение Стьюдента
    """

    typetest((n, a), (int,), {0: "n", 1: "a"})

    if a not in (1, 2, 3):
        raise ValueError(f"Нету в таблице такой доверительной вероятности как {a}")

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
        x = table_students[n][a - 1]
    except KeyError:
        raise ValueError(f"Нету в таблице такой степени свободы как {n}")

    return x


def rotate(tabel: tuple | list) -> tuple | list:
    """Переворачивает таблицу на бок"""

    typetest((tabel,), (tuple, list), {0: "tabel"})

    if type(tabel) is list:
        x = [list(i) for i in zip(*tabel)]
    else:
        x = tuple([i for i in zip(*tabel)])

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

    def _stat1(arg: tuple[int | float, ...] | list[int | float], name: str) -> dict[str, int | float | list]:

        stt1: dict[str, int | float | list] = dict()
        stt1[f"n{name}"] = len(arg)
        stt1[f"sum{name}"] = sum(arg)
        stt1[f"sr{name}"] = stt1[f"sum{name}"] / stt1[f"n{name}"]
        stt1[f"{name}{name}"] = list(map(lambda x: x - stt1[f"sr{name}"], arg), )
        stt1[f"sum{name}{name}"] = sum(stt1[f"{name}{name}"])
        stt1[f"{name}{name}2"] = list(map(lambda x: (x - stt1[f"sr{name}"]) ** 2, arg), )
        stt1[f"sum{name}{name}2"] = sum(stt1[f"{name}{name}2"])
        stt1[f"s0{name}"] = \
            (stt1[f"sum{name}{name}2"] / (stt1[f"n{name}"] * (stt1[f"n{name}"] - 1))) ** (1 / 2)
        stt1[f"{name}2"] = list(map(lambda x: x ** 2, arg))
        stt1[f"sum{name}2"] = sum(stt1[f"{name}2"])
        return stt1

    if not arg2:

        return _stat1(arg1, "X")

    else:
        stt = _stat1(arg1, "X") | _stat1(arg2, "Y")
        stt["XY"] = list(map(lambda x, y: x * y, arg1, arg2))
        stt["sumXY"] = sum(stt["XY"])
        stt["XXYY"] = list(map(lambda x, y: x * y, stt["XX"], stt["YY"]))
        stt["sumXXYY"] = sum(stt["XXYY"])

        return stt


def prim_izmer(
        data: tuple[int | float, ...] | list[int | float],
        accuracy: int | float,
        interval: int = 2, debug: bool = False) -> tuple[float, float] | dict[str, float]:
    """
    Прямые измерения

    slp - случайная погрешность\n
    prp - приборная погрешность\n
    obp - абсолютная погрешность\n

    :param data: данные
    :param accuracy: точность прибора
    :param interval: доверительный интервал
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
        mode: int = 1,
        debug: bool = False) -> (
        (tuple[float, tuple[float, float], tuple[float, float]] |
         tuple[float, tuple[float, float]]
         ) | dict[str, int | float | list]):
    """Метод наименьших квадратов

    :param arg1: значения x
    :param arg2: значения y
    :param mode: 1: y = ax + b, 2: y = ax
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
        mncc1["da"] = stu(stt1["nX"] - 2) * mncc1["sa"]
        mncc1["db"] = stu(stt1["nX"] - 2) * mncc1["sb"]
    else:
        mncc1["r0"] = (stt1["sumXXYY"]) / ((stt1["sumXX2"] ** (1 / 2)) * (stt1["sumYY2"] ** (1 / 2)))
        mncc1["a0"] = stt1["sumXY"] / stt1["sumX2"]
        mncc1["q"] = list(map(lambda x, y: (mncc1["a0"] * x - y) ** 2, arg1, arg2))
        mncc1["sum_q"] = sum(mncc1["q"])
        mncc1["sa"] = (mncc1["sum_q"] / ((stt1["nX"] - 1) * stt1["sumXX2"])) ** (1 / 2)
        mncc1["da"] = stu(stt1["nX"] - 1) * mncc1["sa"]
        return mncc1["r0"], (mncc1["a0"], mncc1["da"])

    if debug:
        return mncc1
    else:
        return mncc1["r0"], (mncc1["a0"], mncc1["da"]), (mncc1["b0"], mncc1["db"])


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

    return convert2number(formula.evalf().__str__()), formula.__str__()


class _LegacyF:
    @staticmethod
    def convert(a):
        """
    Конвертируют строковые значения в числовые в таблице

        :param a:
        :return:
        """
        x = a[0]
        z1 = []
        for i in a[1:]:
            z0 = []
            for q in i:
                try:
                    y = int(q)
                except ValueError:
                    y = float(q)
                z0.append(y)
            z1.append(z0)
        x = [x, *z1]
        return x

    @staticmethod
    def read_tabel(a):
        """
    Читает таблицу из файла
    end для завершения записи элемента, строки, таблицы
    нажми Enter для дублирования значения сверху
    запятая в заголовке для доп описании переменной (сантиметры, килограммы, множители и т.д)

        :param a:
        :return:
        """
        with open(a, encoding='utf-8') as file:
            tabel = [row.strip() for row in file]

        x = [[i.split(",") for i in clr_sp(tabel[0]).split()]]
        y = [clr_sp(i).split() for i in tabel[1:]]

        y0 = rotate(y)[1]
        z1 = -1
        for i in y0:
            z1 += 1
            z2 = -1
            for q in i:
                z2 += 1
                if q == "None":
                    y0[z1][z2] = y0[z1][z2 - 1]

        y = rotate(y0)[1]
        x.extend(y)
        return x

    @staticmethod
    def tabel_to_file(a, b):
        """
    таблицу в фаял

        :param a:
        :param b:
        """
        a = rotate(a)[1]
        x = []
        for i in a:
            y = []
            for q1, q2 in enumerate(i):
                if q1 == 0:
                    t0 = len(q2) - 1
                    t1 = ""
                    for t3, t2 in enumerate(q2):
                        if t3 != t0:
                            t1 += t2 + ","
                        else:
                            t1 += t2
                    y.append(t1)
                else:
                    y.append(q2)
            x.append(y)
        a = x

        x = [max([len(q) for q in i]) for i in a]
        a = [[f"{t:>{q}}" for t in i] for i, q in zip(a, x)]
        a = rotate(a)[1]

        file = open(b, "w", encoding='utf-8')
        for i in a:
            x = ""
            for q in i:
                x += q + " "
            x = x[:-1] + "\n"
            file.write(x)

    @staticmethod
    def make_tabel(a):
        """
    Запись таблицы вручную

        :param a:
        """
        x1 = ""
        y1 = 0
        while True:
            y1 += 1
            z = input(f"x{y1}: ")
            if z == "end":
                break
            x1 += z + " "
        x1 = clr_sp(x1).split()

        print("-" * 30)
        x2 = []
        y2 = 0
        z = input(f"y1|{x1[0]}: ")
        x3 = [*x1[1:], x1[0]]
        while True:
            y2 += 1
            if z == "end":
                break
            z0 = []
            t = y2
            for i in range(y1 - 1):
                z0.append(z)
                if i == y1 - 2:
                    t = y2 + 1
                    print("-" * 30)
                z = input(f"y{t}|{x3[i]}: ")
                if z == "":
                    z = "None"
            x2.append(z0)
        x = [x1, *x2]
        x[0] = [i.split(",") for i in x[0]]

        _LegacyF.tabel_to_file(x, a)

    @staticmethod
    def isee(a, b):
        """
    Мощный срез списков
    a-список, b-срез [1:3, 5, 8:11:2][::-1]

        :param a:
        :param b:
        :return:
        """

        def _fa1(a):
            x = a.replace("]", "[")
            x = x.replace("[[", "[")
            x = x[1:-1].split("[")
            x = [i.split(",") for i in x]
            y = []
            for i in x:
                z = []
                for j in i:
                    x1 = j.count(":")
                    if x1 == 0:
                        j += f":{j}:1"
                    elif x1 == 1:
                        j += ":"
                    z.append(j.split(":"))
                y.append(z)
            return y

        def _fb1(a, b):
            x = []
            y1, y2, y3 = b
            y3 = 1 if not y3 else int(y3)
            y1 = 0 if not y1 and y3 > 0 else len(a) - 1 if not y1 and y3 < 0 else int(y1)
            y2 = len(a) - 1 if not y2 and y3 > 0 else 0 if not y2 and y3 < 0 else int(y2)
            y1 = len(a) + int(y1) if y1 < 0 else y1
            y2 = len(a) + int(y2) if y2 < 0 else y2
            if y3 > 0:
                while y1 <= y2:
                    x.append(a[y1])
                    y1 += y3
            else:
                while y1 >= y2:
                    x.append(a[y1])
                    y1 += y3
            return x

        def _fc1(a, b):
            y = []
            for i in b[0]:
                y.extend(_fb1(a, i))
            if len(b) > 1:
                x1 = b[1:]
                x = []
                for i in y:
                    x.append(_fc1(i, x1))
                y = x
            return y

        return _fc1(a, _fa1(b))

    @staticmethod
    def edit_step(a, b):
        """
    Измена степени у столбцов в таблицы
    a-список, b-кортеж степеней для каждого столбца

        :param a:
        :param b:
        :return:
        """

        def _fa2(a):
            def fx(x):
                h = x * 10 ** a
                return h

            return fx

        def _fb2(a):
            x = []
            for i in a:
                x.append(_fa2(i))
            return x

        b = _fb2(b)
        x0 = a[0]
        x1 = rotate(a[1:])[1]
        for i, q, t in zip(x1, b, range(len(x1))):
            x1[t] = list(map(q, i))
        x = [x0, *rotate(x1)[1]]
        return x

    @staticmethod
    def tpp(*a, b=False):
        x = 'o' if b else None
        import matplotlib.pyplot
        matplotlib.pyplot.plot(*a, marker=x)
        matplotlib.pyplot.minorticks_on()
        matplotlib.pyplot.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        matplotlib.pyplot.grid(which='minor', linestyle='--', linewidth='0.5', color='gray')
        matplotlib.pyplot.show()

    @staticmethod
    def tcpp(*a, b=None):
        if len(a) == 1:
            x = [i for i in range(len(a[0]))]
            y = a[0]
        else:
            x = a[0]
            y = a[1]

        import matplotlib.pyplot
        matplotlib.pyplot.scatter(x, y, s=b)
        matplotlib.pyplot.minorticks_on()
        matplotlib.pyplot.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        matplotlib.pyplot.grid(which='minor', linestyle='--', linewidth='0.5', color='gray')
        matplotlib.pyplot.show()

    @staticmethod
    def pp(a, b=False):
        a = a if not b else rotate(a)[1]
        for i in a:
            print(i)
        print("-" * 30)

    @staticmethod
    def minmax(a, *b):
        b = b if b else [[i for i in range(len(a))]]
        x0 = a[0]
        x1 = b[0]
        y = True
        z = []
        for i, *q in zip(a, *b):
            if y:
                if x0 >= i:
                    x0 = i
                    x1 = q
                else:
                    z.append([x0, *x1])
                    y = False
            else:
                if x0 <= i:
                    x0 = i
                    x1 = q
                else:
                    z.append([x0, *x1])
                    y = True
        return rotate(z)[1][::-1]

    @staticmethod
    def file_to_utf8(file):
        try:
            with open(file) as ff:
                x = ff.read()
        except UnicodeDecodeError:
            with open(file, encoding="utf-8") as ff:
                x = ff.read()
        with open(file, "w", encoding="utf-8") as ff:
            ff.write(x)

    @staticmethod
    def test_open(file):
        try:
            with open(file) as ff:
                ff.read()
                x = True
        except UnicodeDecodeError:
            with open(file, encoding="utf-8") as ff:
                ff.read()
                x = False
        return x

    @staticmethod
    def rea(file, spl=False):
        z = None if _LegacyF.test_open(file) else "utf-8"
        with open(file, encoding=z) as x:
            y = [i.split() if spl else i for i in x]
        return y
