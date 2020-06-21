#
# https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/
# 참고해서 수정해야 함
#
#

import json
import re
from abc import abstractmethod, ABCMeta

class AbstractJson(metaclass=ABCMeta):
    @abstractmethod
    def write_json(self): pass

class WriteJson(AbstractJson):
    def __init__(self, raw_file):
        self.raw_file = raw_file
    
    def write_json(self):
        with open('test.json', 'w') as outfile:
            json.dump(self.raw_file, outfile, indent=4)

class jsonFactory:
    def writedata(self, data):
        res = WriteJson(data)
        return res.write_json()

if __name__ == '__main__':
    data = ''
    with open('input.txt', 'r') as txt:
        for i in txt:
            data += i
    data = re.split('\n', data)
    jf = jsonFactory()
    jf.writedata(data)