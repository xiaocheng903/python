# -*- coding:UTF-8 -*-
import re
import os
import tempfile


class Properties:

    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
#            print(self.properties)
        except Exception as e:
            print(e)
        else:
            fopen.close()

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    def put(self, key, value,flag=True):
        self.properties[key] = value
        #replace_property(self.file_name, key + '=.*', key + '=' + value, flag)
        replace_property(self.file_name, key, value, flag)

def parse(file_name):
    return Properties(file_name)


def replace_property(file_name, key, value, append_on_not_exists=True):
    dirname=os.path.dirname(file_name)
    temp_filename=dirname+'\\temp.properties'
    tmp_file=open(temp_filename,'w')
    if os.path.exists(file_name):
        r_open = open(file_name, 'r')
        for line in r_open:
            if line.find(key)>=0 and not line.strip().startswith('#'):
                valuesplit=line.split('=',1)[1].split('\n')[0]
#                print(valuesplit)
                newline=line.replace(valuesplit,value)
#                print(newline)
                tmp_file.write(newline)
            else:
                tmp_file.write(line)
        r_open.close()
        tmp_file.close()
        if os.path.exists(file_name):
            os.remove(file_name)
        os.rename(temp_filename, file_name)
    else:
        print("file %s not found" % file_name)