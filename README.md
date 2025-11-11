## Work with XML files
=============

## Get diferent information from XML.


Folders you may be interested in:

-  [test_dataset](test_dataset) contains all files for testing.

from xml_worker import Xmlworker()
### Module xml_clear()

data - this xml data with root
This is a mandatory step in work with xml
Этот модуль удаляет все артефакты которые не позволяют обрабатывать xml на python. 
data_clear = xml_worker.xml_clear(data)
Модуль преобразования xml в dict
get_dict(data_clear)

### Получения значения по пути к фрагменту
get_data(dict_data, data_str)

