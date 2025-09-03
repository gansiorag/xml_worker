"""
This module make

Author: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2025//
Ending 2025//

"""

import xmltodict as xd


def dictionary_analysis(str_path: str, level: int, dict_cur: dict, full_info: str):
    """_summary_

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
        full_info += str_path + key + f",Level {new_level} \n"
        if isinstance(dict_cur[key], dict):
            full_info = dictionary_analysis(
                str_path + key + ",", new_level, dict_cur[key], full_info
            )
        if isinstance(dict_cur[key], list):
            full_info = list_analysis(
                str_path + key + ",", new_level, 0, dict_cur[key], full_info
            )
    return full_info


def list_analysis(
    str_path: str, level_dict: int, level_list: int,
    list_cur: list, full_info: str
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
            full_info = dictionary_analysis(str_path, new_level_dict,
                                            row, full_info)
        if isinstance(row, list):
            print(str_path, f", List string {new_level_list}")
            full_info += str_path + f" List string {new_level_list}\n"
            full_info = list_analysis(
                str_path, level_dict, new_level_list, row, full_info
            )
    return full_info


class Xmlworker:
    """Обработчик XML данных"""

    @staticmethod
    def xml_clear(ddd: str) -> str:
        """Очистка xml от артефактов двойных кавычек

        Args:
            ddd (str): XML строка, в которой заменяются дублирующиеся
                       двойные кавычки на &quot;

        Returns:
            str: Очищенная XML строка
        """
        new_str = []
        ser_list = ddd.split(">")
        com_str_error = 0
        for fr1_str in ser_list:
            ser1_list = fr1_str.split("=")
            new_str2 = []
            if len(ser1_list) > 1:
                for fr2_str in ser1_list:
                    if fr2_str.count('"') > 2:
                        com_str_error += 1
                        fr3_str = fr2_str[fr2_str.find('"') + 1:]
                        fr4_str = fr3_str[: fr3_str.rfind('"')].replace('"',
                                                                        "&quot;")
                        serv_str = (
                            "="
                            + fr2_str[: fr2_str.find('"') + 2]
                            + fr4_str
                            + fr2_str[fr2_str.rfind('"'):]
                        )
                        new_str2.append(serv_str)
                    elif 0 < fr2_str.count('"') <= 2:
                        new_str2.append("=" + fr2_str)
                    else:
                        new_str2.append(fr2_str)
            else:
                new_str2.append(ser1_list[0])
            new_str.append("".join(new_str2))
        rez_str = ">".join(new_str)
        return rez_str

    @staticmethod
    def full_struct_xml(data: str):
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
                full_info += key + f",Level {level} \n"
                if isinstance(is_dict[key], dict):
                    full_info = dictionary_analysis(
                        key + ",", level, is_dict[key], full_info
                    )
        if isinstance(is_dict, list):
            print('root_list', f", List string {level}")
            full_info += 'root_list,' + f" List string {level}\n"
            full_info = dictionary_analysis(str_path,
                                            new_level_dict,
                                            row, full_info)
        return full_info


    @staticmethod
    def get_dict(data: str):
        is_dict = xd.parse(data)
        return is_dict
