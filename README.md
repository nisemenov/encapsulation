# Encapsulation

Develop a class with "**full encapsulation**", where access to attributes and modification of data are implemented through method calls. In object-oriented programming, it is customary to begin method names for data retrieval with the word `"get"`, and method names that assign values to properties with the word `"set"`. For example, `get_field`, `set_field`.

## Example of script implementation:

```python
#Input
a = FullEncapsulation('R')
a.set_attr('*')
a.get_attr()
a.d = 1

#Output
Attribute self.__attr_3 = '*' was set.

('_FullEncapsulation__attr_1', 'R')
('_FullEncapsulation__attr_2', 100)
('_FullEncapsulation__attr_3', '*')

Traceback (most recent call last):
  File "/encapsulation/main.py", line 27, in <module>
    a.d = 1
    ^^^
  File "/encapsulation/main.py", line 21, in __setattr__
    raise AttributeError
AttributeError
```
---

Task 6 from course: <https://younglinux.info/oopython/course>
