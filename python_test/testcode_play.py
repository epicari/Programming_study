#
# testcode play by python
#
#
import re
data = ''
with open('input.txt', 'r') as txt:
    for i in txt:
        data += i
data = re.split('\n', data)
a = dict()
a['bread'] = data
print(a.values())