"""
This module make

Author: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2025//
Ending 2025//

"""

import xmltodict as xd
from pprint import pprint


def dictionary_analysis_dist(str_path: str, level: int, dict_cur: dict, full_info: str):
    """Analysis of data in the form of a dictionary.
    return of a full row of decomposed data
    The procedure is used to obtain unique values
    of XML structure fields.

    Args:
        str_path (str): _description_
        level (int): _description_
        dict_cur (dict): _description_
        full_info (str): _description_

    Returns:
        _type_: _description_
    """
    new_level = level + 1
    for key in dict_cur:
        print(str_path + key, f", Level {new_level}")
        full_info += str_path + key + f"^Level {new_level} \n"
        if isinstance(dict_cur[key], dict):
            full_info = dictionary_analysis_dist(
                str_path + key + "^", new_level, dict_cur[key], full_info
            )
        if isinstance(dict_cur[key], list):
            full_info = list_analysis_dist(
                str_path + key + "^", new_level, dict_cur[key], full_info
            )
    return full_info


def dictionary_analysis_value(
    str_path: str, level: int, dict_cur: dict, full_info: str
):
    """Analysis of data in the form of a dictionary.
    return of a full row of decomposed data with value atributs.
    The procedure is used to obtain values of atributes of XML structure fields.

    Args:
        str_path (str): _description_
        level (int): _description_
        dict_cur (dict): _description_
        full_info (str): _description_

    Returns:
        _type_: _description_
    """
    new_level = level + 1
    for key in dict_cur:
        print(str_path + key, f", Level {new_level}")
        full_info += str_path + key + f"^Level {new_level} \n"
        if isinstance(dict_cur[key], dict):
            full_info = dictionary_analysis_value(
                str_path + key + "^", new_level, dict_cur[key], full_info
            )
        if isinstance(dict_cur[key], list):
            full_info = list_analysis_value(
                str_path + key + "^", new_level, 0, dict_cur[key], full_info
            )
        if isinstance(dict_cur[key], str):
            full_info = get_value(str_path, dict_cur[key], key, level, full_info)
    return full_info


def dictionary_analysis(str_path: str, level: int, dict_cur: dict, full_info: str):
    """Analysis of data in the form of a dictionary.
    return of a full row of decomposed data with value atributs.
    The procedure is used to obtain values of atributes of XML structure fields.

    Args:
        str_path (str): _description_
        level (int): _description_
        dict_cur (dict): _description_
        full_info (str): _description_

    Returns:
        _type_: _description_
    """
    new_level = level + 1
    for key in dict_cur:
        print(str_path + key, f", Level {new_level}")
        full_info += str_path + key + f"^Level {new_level} \n"
        if isinstance(dict_cur[key], dict):
            full_info = dictionary_analysis(
                str_path + key + "^", new_level, dict_cur[key], full_info
            )
        if isinstance(dict_cur[key], list):
            full_info = list_analysis(
                str_path + key + "^", new_level, 0, dict_cur[key], full_info
            )
        # if isinstance(dict_cur[key], str):
        #     full_info = get_value(str_path, dict_cur[key],
        #                           key, level, full_info)
    return full_info


def list_analysis(
    str_path: str, level_dict: int, level_list: int, list_cur: list, full_info: str
) -> str:
    """
    Analysis of data in the form of a list.
    return of a full row of decomposed data.
    The procedure is used to obtain full path of atributes of XML structure fields.

    Args:
        str_path (str): Текущий путь в структуре данных.
        level_dict (int): Уровень вложенности словаря.
        level_list (int): Уровень вложенности списка.
        list_cur (list): Текущий список для анализа.
        full_info (str): Накопленная информация.
    Returns:
        str: Обновленная накопленная информация.
    """
    for idx, item in enumerate(list_cur, start=1):
        # Формируем сообщение о текущем элементе списка
        info_line = f"{str_path} List string {idx}"
        print(info_line)
        full_info += info_line + "\n"
        if isinstance(item, dict):
            # Передаём текущий уровень словаря без изменений
            full_info = dictionary_analysis(str_path, level_dict, item, full_info)
        elif isinstance(item, list):
            # Для вложенного списка
            full_info = list_analysis(str_path, level_dict, idx, item, full_info)
    return full_info


def list_analysis_value(
    str_path: str, level_dict: int, level_list: int, list_cur: list, full_info: str
):
    """_summary_

    Args:
        str_path (str): Текущий путь в структуре данных.
        level_dict (int): Уровень вложенности словаря.
        level_list (int): Уровень вложенности списка.
        list_cur (list): Текущий список для анализа.
        full_info (str): Накопленная информация.

    Returns:
        full_info (str): Обновленная накопленная информация
    """
    new_level_dict = 0
    new_level_list = 0
    for row in list_cur:
        new_level_list = new_level_list + 1
        if isinstance(row, dict):
            new_level_dict = level_dict
            print(str_path, f", List string {new_level_list}")
            full_info += str_path + f" List string {new_level_list}\n"
            full_info = dictionary_analysis_value(
                str_path, new_level_dict, row, full_info
            )
        if isinstance(row, list):
            print(str_path, f", List string {new_level_list}")
            full_info += str_path + f" List string {new_level_list}\n"
            full_info = list_analysis_value(
                str_path, level_dict, new_level_list, row, full_info
            )

    return full_info


def list_analysis_dist(
    str_path: str, level_dict: int, list_cur: list, full_info: str
) -> str:
    """
    Анализирует список, рекурсивно обрабатывая вложенные словари и списки.
    Args:
        str_path (str): Текущий путь в структуре данных.
        level_dict (int): Уровень вложенности словаря.
        level_list (int): Уровень вложенности списка.
        list_cur (list): Текущий список для анализа.
        full_info (str): Накопленная информация.
    Returns:
        str: Обновленная накопленная информация.
    """
    for item in list_cur:
        # Формируем сообщение о текущем элементе списка
        info_line = f"{str_path} List string"
        print(info_line)
        full_info += info_line + "\n"
        if isinstance(item, dict):
            # Передаём текущий уровень словаря без изменений
            full_info = dictionary_analysis_dist(str_path, level_dict, item, full_info)
        elif isinstance(item, list):
            # Для вложенного списка
            full_info = list_analysis_dist(str_path, level_dict, item, full_info)
    return full_info


def get_value(str_path: str, is_dict: str, key: str, level, full_info: str):
    full_info += str_path + key + "^" + is_dict + f"^Level {level + 1} \n"
    return full_info


class Xmlworker:
    """Обработчик XML данных"""

    @staticmethod
    def xml_clear(ddd: str) -> str:
        """Очистка XML от артефактов с дублирующимися двойными кавычками.
        Заменяет все двойные кавычки внутри значений атрибутов (кроме внешних)
        на &quot;.
        Args:
            ddd (str): Исходная XML-строка.
        Returns:
            str: Очищенная XML-строка.
        """
        parts = ddd.split(">")
        cleaned_parts = []
        for part in parts:
            segments = part.split("=")
            if len(segments) == 1:
                # Нет атрибутов, просто добавляем часть как есть
                cleaned_parts.append(segments[0])
                continue
            new_segments = [segments[0]]  # первая часть до первого '='
            for seg in segments[1:]:
                quote_count = seg.count('"')
                if quote_count > 2:
                    # Есть лишние двойные кавычки внутри значения
                    first_quote_idx = seg.find('"')
                    last_quote_idx = seg.rfind('"')
                    # Внутренние кавычки заменяем на &quot;
                    inner = seg[first_quote_idx + 1 : last_quote_idx].replace(
                        '"', "&quot;"
                    )
                    # Собираем обратно: = + открывающая кавычка + очищенное
                    # содержимое + закрывающая кавычка + остаток
                    fixed = (
                        "=" + seg[: first_quote_idx + 1] + inner + seg[last_quote_idx:]
                    )
                    new_segments.append(fixed)
                elif 0 < quote_count <= 2:
                    # Значение с корректным количеством кавычек, просто
                    # добавляем с '='
                    new_segments.append("=" + seg)
                else:
                    # Нет кавычек, добавляем как есть
                    new_segments.append(seg)
            cleaned_parts.append("".join(new_segments))
        return ">".join(cleaned_parts)

    @staticmethod
    def full_dist_struct_xml(data: str, full_path_file=""):
        """_summary_

        Args:
            data (str): _description_
        """
        level = 0
        is_dict = xd.parse(data)
        full_info = ""
        if isinstance(is_dict, dict):
            for key in is_dict:
                print(key, f" Level {level}")
                full_info += key + f"^Level {level} \n"
                if isinstance(is_dict[key], dict):
                    full_info = dictionary_analysis_dist(
                        key + "^", level, is_dict[key], full_info
                    )
        if isinstance(is_dict, list):
            print("root_list List string")
            full_info += "root_list, List string\n"
            full_info = list_analysis_dist("root_list", level, is_dict,
                                           full_info)
        full_info_set = sorted(set(full_info.split("\n")))
        if full_path_file:
            with open(full_path_file, "w", encoding="utf-8") as r_f:
                num_str = 0
                for row in full_info_set:
                    r_f.write(str(num_str) + "^" + row + "\n")
                    num_str += 1
        return full_info

    @staticmethod
    def full_struct_xml(data: str, full_path_file=""):
        """_summary_

        Args:
            data (str): _description_
        """
        level = 0
        is_dict = xd.parse(data)
        full_info = ""
        if isinstance(is_dict, dict):
            for key in is_dict:
                print(key, f" Level {level}")
                full_info += key + f"^Level {level} \n"
                if isinstance(is_dict[key], dict):
                    full_info = dictionary_analysis(
                        key + "^", level, is_dict[key], full_info
                    )
        if isinstance(is_dict, list):
            print("root_list", f", List string {level}")
            full_info += "root_list," + f" List string {level}\n"
            full_info = list_analysis("root_list", level, level, is_dict, full_info)
        if full_path_file:
            with open(full_path_file, "w", encoding="utf-8") as r_f:
                num_str = 0
                for row in full_info.split("\n"):
                    r_f.write(str(num_str) + "^" + row + "\n")
                    num_str += 1
        return full_info

    @staticmethod
    def full_struct_xml_value(data: str, full_path_file=""):
        """_summary_

        Args:
            data (str): _description_
        """
        level = 0
        is_dict = xd.parse(data)
        full_info = ""
        if isinstance(is_dict, dict):
            for key in is_dict:
                # print(key, f" Level {level}")
                full_info += key + f"^Level {level} \n"
                if isinstance(is_dict[key], dict):
                    full_info = dictionary_analysis_value(
                        key + "^", level, is_dict[key], full_info
                    )
        if isinstance(is_dict, list):
            # print("root_list", f", List string {level}")
            full_info += "root_list," + f" List string {level}\n"
            full_info = list_analysis_value(
                "root_list", level, level, is_dict, full_info
            )
        if isinstance(is_dict, str):
            full_info = get_value("root^", is_dict, "root", level, full_info)
        if full_path_file:
            with open(full_path_file, "w", encoding="utf-8") as r_f:
                num_str = 0
                for row in full_info.split("\n"):
                    r_f.write(str(num_str) + "^" + row + "\n")
                    num_str += 1
        return full_info

    @staticmethod
    def get_dict(data: str):
        is_dict = xd.parse(data)
        return is_dict

    @staticmethod
    def anl_list(path_full: list, step: int, i_d: list):
        """
        Рекурсивно обходит список, содержащий строки, словари и вложенные списки.
        
        Как только встречает строку — сразу возвращает её.
        Для словарей и списков делает рекурсивный вызов.
        Если строка не найдена — возвращает None.
        """        
        dd = None
        for index, d_l in enumerate(i_d):
            if isinstance(d_l, str):
                return d_l            
            elif isinstance(d_l, list):
                print(f'List_2 {index}')
                dd = Xmlworker.anl_list(path_full, step, d_l)
            if isinstance(d_l, dict):
                dd = Xmlworker.anl_dict(path_full, step, d_l)
        return dd

    @staticmethod
    def anl_dict(path_full: list, step: int, i_d: dict):
        """Раскладывает словарь до конечного значения

        Args:
            path_full (list): Полный путь до значения
            step (int): номер шага полного пути
            i_d (dict): анализируемая структура

        Raises:
            KeyError: _description_

        Returns:
            _type_: возвращает значение шага
        """
        # print('path_full => ', path_full)
        # print('step => ', step)
        # print('==== anl_dict ====')
        if step == len(path_full):
            key = path_full[step - 1]
            print(f'Value key {key}')
            # print(i_d)
            if key in i_d:
                pprint(i_d[key])
                return i_d[key]
            elif path_full[step - 1] in i_d:
                # print(key, ' ==> ', i_d[path_full[step - 2]][key])
                return i_d[path_full[step - 2]][key]
            elif path_full[step - 2] in i_d:
                if isinstance(i_d[path_full[step - 2]][key], str):
                    print(i_d[path_full[step - 2]][key])
                    return i_d[path_full[step - 2]][key]
                else:
                    print(i_d[path_full[step - 1]][key])
                    return i_d[path_full[step - 1]][key]
            else:
                return print(i_d)
        else:
            key = path_full[step]
            if isinstance(i_d, dict):
                return Xmlworker.anl_dict(path_full, step + 1, i_d)
            elif isinstance(i_d[key], list):
                dd = Xmlworker.anl_list(path_full, step, i_d[key])
                return dd
            elif isinstance(i_d[key], str):
                raise KeyError(f"Value step {step}: {key} is {i_d[key]}")

    @staticmethod
    def get_data_field(is_da: dict, data_str: str):
        """Получение значения поля по известному пути к нему

        Args:
            is_da (dict): Словарь данных
            data_str (str): строка описывающая путь по словарю
            пример - ЕГРЮЛ^СвЮЛ^СвЗапЕГРЮЛ^СведПредДок^НаимДок

        Raises:
            ValueError: Проверяет что входные данные являются словарем

        Returns:
            _type_: Ничего не возвращает
        """        
        if not isinstance(is_da, dict):
            raise ValueError("is_da must be a dictionary")
        if not data_str or not isinstance(data_str, str):
            return None

        path = [part.strip() for part in data_str.strip().split('^') if part.strip()]
        if not path:
            return None
        k_l = 0
        current = is_da
        for i, key in enumerate(path):
            print(f' {i} == {key}')
            if key not in current:
                print(f"Error - field '{'^'.join(path[:i+1])}' not found!")
                return None
            current = current[key]
            if isinstance(current, list):
                print(f'List {k_l}')
                dd = Xmlworker.anl_list(path, i, current)
                k_l += 1
                return dd
        return current
