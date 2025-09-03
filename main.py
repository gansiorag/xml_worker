'''
This module make

Author: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2025/09/03
Ending 2025//

'''

from set_prog.base_class import XML_WORKER


xml_worker = XML_WORKER()

with open('/home/gansior/MyProject/xml_worker/test_datasets/1020700588688.xml', 'r', encoding='utf-8') as i_f:
    data = i_f.read()
    data_clear = xml_worker(data)
