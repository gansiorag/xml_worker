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
name_file = '/home/gansior/MyProject/xml_worker/test_datasets/push_mes_egrul.xml'
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/schemas_egrul/fns-egrulotn-types.xsd'
# name_file = '/home/gansior/MyProject/xml_worker/test_datasets/schemas_egrul/schemas.xsd'
with open(name_file, 'r', encoding='utf-8') as i_f:
    data = i_f.read()
    data_clear = xml_worker.xml_clear(data)
    f_str = xml_worker.full_struct_xml(data_clear)
    name_rezult = name_file.split('/')[-1].split('.')[0]
    with open(f'rezult_{name_rezult}.csv', 'w', encoding='utf-8') as r_f:
        num_str = 0
        for row in f_str.split('\n'):
            r_f.write(str(num_str) + ',' + row + '\n')
            num_str += 1
