# -*- coding: utf-8 -*-

def change_string_to_int(data):
    if data is None or data == '':
        new_data = ot
    elif isinstance(data, (int, float)):
        new_data = round(data)
    elif isinstance(data, str):
        if data.isdigit():
            new_data = int(data)
        else:
            float_data = data.split(sep='.')
            if len(float_data)==2 and float_data[0].isdigit() and float_data[1].isdigit():
                new_data = round(float(data))     
            else:
                raise Exception('please check the input data')
    else:
        raise Exception('please check the input data')
    return new_data
a = ''

new_data = change_string_to_int(a)
print(new_data)