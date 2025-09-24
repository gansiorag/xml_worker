'''
This module make

Author: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2025/09/03
Ending 2025//

'''
import sys
import os


current_directory = os.getcwd()
print(current_directory)
sys.path.append(current_directory)


from set_prog.base_class import Xmlworker

xml_worker = Xmlworker()
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/1020700588688.xml'
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/push_mes_egrul.xml'
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/13673441xsd/VO_RUGF_2_311_26_04_07_01.xsd'
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/schemas_egrul/fns-egrulotn-types.xsd'
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/schemas_egrul/schemas.xsd'
name_file = '/home/gansior/MyProject/parser_xml_egrul_egrip/dataset/egrul/aronov/7107133140.xml'
with open(name_file, 'r', encoding='utf-8') as i_f:
    data = i_f.read()
    data_clear = xml_worker.xml_clear(data)
    dict_data = xml_worker.get_dict(data_clear)
    print(dict_data)

    # name_file_rezult = f'rezult_{name_file.split('/')[-1].split('.')[0]}_full.csv'
    # f_str = xml_worker.full_struct_xml(data_clear, name_file_rezult)
    
    # name_file_rezult = f'rezult_{name_file.split('/')[-1].split('.')[0]}_value.csv'
    # f_str = xml_worker.full_struct_xml_value(data_clear, name_file_rezult)  # Получение полной структуры XML с

    name_file_rezult = f'rezult_{name_file.split('/')[-1].split('.')[0]}_dist.csv'
    f_str = xml_worker.full_dist_struct_xml(data_clear, name_file_rezult)  # Получение полной структуры XML с уникальными атрибутами
