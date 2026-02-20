Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict{}
a={'name':'emmanuel','year':2026,'month':2}
print(a)
{'name': 'emmanuel', 'year': 2026, 'month': 2}
type(a)
<class 'dict'>
b={'name','month','year'}
type(b)
<class 'set'>
a={'name':'emmanuel','year':2026,'month':2}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['emmanuel', 2026, 2])
a.items()
dict_items([('name', 'emmanuel'), ('year', 2026), ('month', 2)])
#accessing
a={'name':'emmanuel','date':2026}
a['name']
'emmanuel'
a[2026]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[2026]
KeyError: 2026
#update
a={'name':'emmanuel','year':2026,'month':2}
a.update({'mailid:emmanuel@.com'})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({'mailid:emmanuel@.com'})
ValueError: dictionary update sequence element #0 has length 20; 2 is required
a.update({'mailid':'emmanuel@.com'})
a
{'name': 'emmanuel', 'year': 2026, 'month': 2, 'mailid': 'emmanuel@.com'}
>>> a.update({'age':22},{'type':'dic'})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.update({'age':22},{'type':'dic'})
TypeError: update expected at most 1 argument, got 2
>>> a.update({'age':22,'type':'dic'})
>>> a
{'name': 'emmanuel', 'year': 2026, 'month': 2, 'mailid': 'emmanuel@.com', 'age': 22, 'type': 'dic'}
>>> a={'time':10,'hours':12,'sec':60}
>>> a.setdefault('min',60)
60
>>> a
{'time': 10, 'hours': 12, 'sec': 60, 'min': 60}
>>> #pop and popitem
>>> a={'colour:blue','shoe':nike}
SyntaxError: invalid syntax
>>> a={'colour:blue','shoe':'nike','hi':'hello'}
SyntaxError: invalid syntax
>>> a={'colour':'blue','shoe':'nike','hi':'hello'}
>>> a.pop('colour')
'blue'
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.popitem()
('hi', 'hello')
>>> a
{'shoe': 'nike'}
