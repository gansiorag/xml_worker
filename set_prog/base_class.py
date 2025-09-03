"""
This module make

Author: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2025//
Ending 2025//

"""


class XML_WORKER:
    """Обработчик XML данных"""

    @staticmethod
    def xml_clear(ddd: str) -> str:
        """Очистка xml от артефактов двойных кавычек

        Args:
            ddd (str): XML строка, в которой заменяются дублирующиеся двойные кавычки на &quot;

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
                        fr3_str = fr2_str[fr2_str.find('"') + 1 :]
                        fr4_str = fr3_str[: fr3_str.rfind('"')].replace('"', "&quot;")
                        serv_str = (
                            "="
                            + fr2_str[: fr2_str.find('"') + 2]
                            + fr4_str
                            + fr2_str[fr2_str.rfind('"') :]
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
