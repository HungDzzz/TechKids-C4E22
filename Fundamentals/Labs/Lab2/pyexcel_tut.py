import pyexcel
from collections import OrderedDict # int,str.list ,int("78") , giup hien thi theo thu tu trong dict
data = [
    OrderedDict({
        'Name': 'Hung',
        'Age':22,
        'City':'Ha Noi'
    }),
    OrderedDict({
        'Name':'Hau',
        'Age':22,
        'City':'Ha Noi'
    }),
    OrderedDict({
        'Name': 'Anh',
        'Age':22,
        'City':'Ha Noi'
    })
]
pyexcel.save_as(records=data, dest_file_name = "sample.xlsx")