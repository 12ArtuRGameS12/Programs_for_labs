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


def clr_sp(text: str, *car_cls: str) -> str:
    """Чистит водимую строку от лишних пробелов"""

    typetest((text, *car_cls), (str,), {0: "text"})

    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    for i in car_cls:
        while text.find(f" {i}") != -1:
            text = text.replace(f" {i}", f"{i}")
        while text.find(f"{i} ") != -1:
            text = text.replace(f"{i} ", f"{i}")
    if text[0] == " ":
        text = text[1:]
    if text[-1] == " ":
        text = text[:-1]

    return text


def sup_rep(text: str, rep: dict[str, str]) -> str:
    """Массовая замена символов

    :param text: исходный текст
    :param rep: словарь замен
    :return: изменённый текст
    """

    typetest((rep,), (dict,), {0: "rep"})
    typetest((text, *rep,), (str,), {0: "text"})
    typetest(([rep[i] for i in rep]), (str,))

    new_text = str()
    for i in text:
        for q in rep:
            if i == q:
                new_text += rep[q]
                break
        else:
            new_text += i
    return new_text


def rotate(tabel: tuple | list) -> tuple | list:
    """Переворачивает таблицу на бок"""

    typetest((tabel,), (tuple, list), {0: "tabel"})

    if type(tabel) is list:
        x = [list(i) for i in zip(*tabel)]
    else:
        x = tuple([i for i in zip(*tabel)])

    return x


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
