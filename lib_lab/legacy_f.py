from lib_lab import *
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

    tabel_to_file(x, a)


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


def tpp(*a, b=False):
    x = 'o' if b else None
    import matplotlib.pyplot
    matplotlib.pyplot.plot(*a, marker=x)
    matplotlib.pyplot.minorticks_on()
    matplotlib.pyplot.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    matplotlib.pyplot.grid(which='minor', linestyle='--', linewidth='0.5', color='gray')
    matplotlib.pyplot.show()


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


def pp(a, b=False):
    a = a if not b else rotate(a)[1]
    for i in a:
        print(i)
    print("-" * 30)


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


def file_to_utf8(file):
    try:
        with open(file) as ff:
            x = ff.read()
    except UnicodeDecodeError:
        with open(file, encoding="utf-8") as ff:
            x = ff.read()
    with open(file, "w", encoding="utf-8") as ff:
        ff.write(x)


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


def rea(file, spl=False):
    z = None if test_open(file) else "utf-8"
    with open(file, encoding=z) as x:
        y = [i.split() if spl else i for i in x]
    return y
