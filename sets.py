Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets{}
a={3,3.5,'raju',8+6j,True,False}
print(a)
{False, True, 3.5, 'raju', 3, (8+6j)}
type(a)
<class 'set'>
b={9,8,7,6,5,9,8,7}
print(b)
{5, 6, 7, 8, 9}
type(b)
<class 'set'>
#and and subset
a={4,5,9,6,7,8}
a.add(30)
a
{4, 5, 6, 7, 8, 9, 30}
a={9,8,7,6,5,4,}
b={6,5,4}
b.issubset(a)
True
a.issubset(b)
False
a={2,3,4,5,6,7}
b={2,3,9,8}
b.subset(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.subset(a)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
b.issubset(a)
False
a.issubset(b)
False
#superset
a={1,2,3,4,5,6}
b={1,2,3,8}
a.issuperset(b)
False
a={1,2,3,4,5,6,7}
b={5,6,7}
a.issuperset(b)
True
#union()
a={2,3,4,5,6,7,8}
b={2,3,4,9,0,1}
a.union(b)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#intersection
a={1,2,3,4,5,6,7}
b={1,2,3,8,9,0}
a.intersection(b)
{1, 2, 3}
#difference()
a={2,3,4,5,6,7,8}
b={2,4,11,12,8,9,0}
a.difference(b)
{3, 5, 6, 7}
b.difference(a)
{0, 9, 11, 12}
#update()
a={10,11,12,13,14,15,16}
b={2,3,4,5,11,12,13,14}
a.union(b)
{2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16}
a
{16, 10, 11, 12, 13, 14, 15}
a.update(b)
a
{2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16}
a
{2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16}
b.update(a)
b
{2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16}
a={4,5,6,7,8,9}
b={1,2,3,4,5,6,7,8,9}
a.difference_update(b)
a
set()
a={2,3,4,5,6,7,8}
b={1,2,5,7,8,9,0}
a.difference_update(b)
a
{3, 4, 6}
b.difference_update(a)
b
{0, 1, 2, 5, 7, 8, 9}
#symmetric difference
a={3,4,5,6,7,8,9}
b={1,2,3,4,9,0,11}
a.symmetric_difference(b)
{0, 1, 2, 5, 6, 7, 8, 11}
b.symmetric_difference(a)
{0, 1, 2, 5, 6, 7, 8, 11}
a
{3, 4, 5, 6, 7, 8, 9}
#symmetric difference update()
a={1,3,4,5,7,9,11,13}
b={2,3,4,6,8,10,12}
a.symmetric_difference_update(b)
a
{1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13}
a
{1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b
{2, 3, 4, 6, 8, 10, 12}
b.symmetric_difference_update(a)
b
{1, 3, 4, 5, 7, 9, 11, 13}
#intersection update
a{7,8,9,11,12,13,14,16}
SyntaxError: invalid syntax
a={6,7,8,9,11,12,13,14}
b={1,2,3,4,5,6,7,8}
a.intersection_update(b)
a
{8, 6, 7}
b.intersection_update(a)
b
{8, 6, 7}
#pop
a={1,2,3,4,5,6,7}
a.pop()
1
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
a
{2, 3, 4, 6, 7}
#copy
a={3,4,5,6,7}
a.copy()
{3, 4, 5, 6, 7}
b.copy(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    b.copy(a)
TypeError: set.copy() takes no arguments (1 given)
b.copy()
{8, 6, 7}
#copy()
a={3,4,5,6,7}
a.copy()
{3, 4, 5, 6, 7}
a.clear()
a
set()
b=set()
b.add(23)
>>> b
{23}
>>> b.discard()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    b.discard()
TypeError: set.discard() takes exactly one argument (0 given)
>>> b.discard(23)
>>> b
set()
>>> a={3,4,5,6,7,8}
>>> b={2,4,5,7,0}
>>> a.isdisjoint(b)
False
>>> a={1,2,3,4}
>>> b={6,7,8,9}
>>> a.isdisjoint(b)
True
>>> a={1,2,3,4,56}
>>> len(a)
5
>>> a.count(56)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.count(56)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(4)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
