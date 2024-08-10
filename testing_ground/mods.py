import copy

import lib_lab as lb


def nakop(a):
    y = []
    x = 0
    for i in a:
        x += i
        y.append(x)
    return y


def rn(a, b=0):
    x = 10 ** (b + 1)
    y = int(a * x)
    z = y % 10
    if z >= 5:
        y += 10
    y -= z
    return y / x


def delta(x, y, z):
    a = lb.mnc(x, y, debug=True)
    b = lb.stat(x, y)
    c = (a["sum_q"] / (b["nX"] - 2) * (1 / b["nX"] + (z - b["srX"]) ** 2 / b["sumXX2"])) ** (1 / 2) * lb.stu(
        b["nX"] - 2)
    return c


class Table:
    def __init__(self, data):
        self.data = data
        self.nerav_izmer = False
        self.pr = True
        self.name = None
        # self.para = {}

    def convert(self):
        for i in self.data:
            x = self.data[i]

            def y(z):
                return x[1] * 10 ** z, x[2] * 10 ** z
            match x[0]:
                case "см":
                    self.data[i] = ["м", *y(-2)]
                case "мм":
                    self.data[i] = ["м", *y(-3)]
                case "мН":
                    self.data[i] = ["Н", *y(-3)]
                case "г":
                    self.data[i] = ["кг", *y(-3)]

        return self

    def ptabel(self, format_st="f"):
        data = copy.deepcopy(self.data)
        for i in data:
            data[i][1] = format(data[i][1], format_st)
            data[i][2] = format(data[i][2], format_st)
        mymax = [0, 0, 0, 0]
        for i in data:
            x, y, z = [len(q.__str__()) for q in data[i]]
            if len(i) > mymax[0]: mymax[0] = len(i)
            if x > mymax[1]: mymax[1] = x
            if y > mymax[2]: mymax[2] = y
            if z > mymax[3]: mymax[3] = z
        for i in data:
            print(
                f"| {i:<{mymax[0]}} | {data[i][0]:<{mymax[1]}} | {data[i][1]:>{mymax[2]}} | {data[i][2]:>{mymax[3]}} |")
        print("-" * 30)

        return self

    def solve(self, formula: str, var: dict[str, list[str,]], nerav_izmer: bool = False, pr: bool = True):

        max_var = max([len(var[i]) for i in [*var]])
        tabel_var = list()
        for j in range(max_var):
            dd: dict = dict()
            for d in range(2):
                for i in var:
                    name = "d" * d + i
                    varibal = self.data[var[i][j]][d + 1] if type(var[i][j]) == str else var[i][j][d]
                    dd.update({name: varibal})
            tabel_var.append(dd)

        y = lb.cosn_izmer_formula(formula, *var)
        tabel_data = [[lb.formula_exe(formula, i)[0], lb.formula_exe(y, i)[0]] for i in tabel_var]

        x = lb.nerav_izmer(*lb.rotate(tabel_data)) if nerav_izmer else None
        if pr:
            print(formula)

            if len(tabel_data) > 1 and type(tabel_data[0]) in (list, tuple):
                for i, j in zip(tabel_data, range(1, len(tabel_data) + 1)):
                    print(f"{j}) {i}")
            else:
                print(f"{tabel_data[0][0]} ± {tabel_data[0][1]}")

            if nerav_izmer:
                print("|" * 30)
                print(f"{x[0]} ± {x[1]}")
            print("-" * 30 + "\n", sep="", end="")
        return tabel_data, x

    def __mul__(self, other):
        if other != 0:
            for i in self.data:
                x = self.data[i]
                self.data[i] = [x[0] + f" * 10**{other}", x[1] * 10 ** other, x[2] * 10 ** other]
        return self

    def __enter__(self):
        class X:
            def __init__(other_self):
                other_self.nerav_izmer = self.nerav_izmer
                other_self.pr = self.pr
                other_self.name = self.name
                other_self.var = None
                other_self.formula = None
                other_self.raz = None

        self.x = X()
        return self.x

    def __exit__(self, exc_type, exc_val, exc_tb):
        y = self.x
        x, z = self.solve(y.formula, y.var, y.nerav_izmer, y.pr)
        if y.name:
            if len(y.name) > 1:
                for i, j in zip(y.name, x):
                    self.data[i] = [y.raz, *j]
            else:
                if y.nerav_izmer:
                    self.data[y.name[0]] = [y.raz, *z]
                else:
                    self.data[y.name[0]] = [y.raz, *x[0]]
        del self.x


def graf(*points, major, minor):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator

    for i in points:
        plt.scatter(*i)

    # Устанавливаем расстояние между мажорными делениями по оси X и Y
    plt.gca().xaxis.set_major_locator(MultipleLocator(major[0]))
    plt.gca().yaxis.set_major_locator(MultipleLocator(major[1]))

    # Устанавливаем расстояние между второстепенными делениями по осям X и Y
    plt.gca().xaxis.set_minor_locator(MultipleLocator(minor[0]))
    plt.gca().yaxis.set_minor_locator(MultipleLocator(minor[1]))

    # Добавляем сетку для мажорных и второстепенных делений
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.grid(which='minor', linestyle='--', linewidth='0.5', color='gray')

    plt.show()
