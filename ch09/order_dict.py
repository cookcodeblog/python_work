# 9-13 OrderedDict
from collections import OrderedDict

staffs = OrderedDict()
staffs['Will'] = 'SCS'
staffs['Lev'] = 'CS'
staffs['Rob'] = 'SSE'

for name, title in staffs.items():
    print(name.title() + " is a " + title.upper())

