Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionery
a={'name':'raju','city':'mandapeta','mail':'@raju.com'}
a.get('name')
'raju'
a.copy()
{'name': 'raju', 'city': 'mandapeta', 'mail': '@raju.com'}
a.clear()
a
{}
b={}
b.update({'mobile no':1425365768})
b
{'mobile no': 1425365768}
>>> a={'name':'raju','city':'mandapeta','mail':'@raju.com'}
>>> print(a)
{'name': 'raju', 'city': 'mandapeta', 'mail': '@raju.com'}
>>> a={'name':'raju','city':'mandapeta','mail':'@raju.com','name':'raju'}
>>> a
{'name': 'raju', 'city': 'mandapeta', 'mail': '@raju.com'}
>>> a={'name':'raju','city':'mandapeta','mail':'@raju.com','name1':'raju'}
>>> print(a)
{'name': 'raju', 'city': 'mandapeta', 'mail': '@raju.com', 'name1': 'raju'}
>>> 
>>> a={'idnos':[11,12,13],'name':[raju,kevin,sasi],'city':[hyd,vij,rjy]}
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a={'idnos':[11,12,13],'name':[raju,kevin,sasi],'city':[hyd,vij,rjy]}
NameError: name 'raju' is not defined
>>> 
>>> 
>>> a={'idnos':[11,12,13],'name':['raju','kevin','sasi'],'city':['hyd','vij','rjy']}
>>> print(a)
{'idnos': [11, 12, 13], 'name': ['raju', 'kevin', 'sasi'], 'city': ['hyd', 'vij', 'rjy']}
>>> a.key()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> a.keys()
dict_keys(['idnos', 'name', 'city'])
>>> a.values()
dict_values([[11, 12, 13], ['raju', 'kevin', 'sasi'], ['hyd', 'vij', 'rjy']])
>>> a.items()
dict_items([('idnos', [11, 12, 13]), ('name', ['raju', 'kevin', 'sasi']), ('city', ['hyd', 'vij', 'rjy'])])
