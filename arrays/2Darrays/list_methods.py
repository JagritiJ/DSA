# $ python
# Python 3.9.0a1 (tags/v3.9.0a1:fd75708, Nov 19 2019, 18:15:20) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a =[]
# >>> print a
#   File "<stdin>", line 1
#     print a
#           ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
# >>> print(a)
# []
# >>> a.ppend(20)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'ppend'
# >>> a.append(20) 
# >>> print(a)     
# [20]
# >>> a.append(45)
# >>> a.append(90)
# >>> print(a)
# [20, 45, 90]
# >>> a.insert(2, 65)
# >>> print(a)
# [20, 45, 65, 90]
# >>> a.insert(2, 89)
# >>> print(a)
# [20, 45, 89, 65, 90]
# >>> a.extend([6, 23, 37])
# >>> a
# [20, 45, 89, 65, 90, 6, 23, 37]
# >>> a.pop()
# 37
# >>> a       
# [20, 45, 89, 65, 90, 6, 23]
# >>> a.remove(65)
# >>> a
# [20, 45, 89, 90, 6, 23]
# >>> a.add(78)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'add'
# >>> a.delete()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'delete'
# >>> a.append()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: list.append() takes exactly one argument (0 given)
# >>> a
# [20, 45, 89, 90, 6, 23]
# >>> a.index(45)
# 1
# >>> a.sort()
# >>> a
# [6, 20, 23, 45, 89, 90]
# >>> a.sort(descending=true)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined
# >>> a.sort(descending)      
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'descending' is not defined
# >>> a.sort()           
# >>> a
# [6, 20, 23, 45, 89, 90]
# >>> sorted(a)
# [6, 20, 23, 45, 89, 90]
# >>> len(a)
# 6
# >>> a.length
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'length'
# >>> st="wertt"
# >>> st.length
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'length'
# >>> a
# [6, 20, 23, 45, 89, 90]
# >>> a.pop(20)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: pop index out of range
# >>> a.pop(3)
# 45
# >>> a
# [6, 20, 23, 89, 90]
# >>> max(a)
# 90
# >>> min(a)
# 6
# >>> sum(a)
# 228
# >>> count(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'count' is not defined
# >>> a
# [6, 20, 23, 89, 90]
# >>> a.reverse()
# >>> a
# [90, 89, 23, 20, 6]
# >>> ^A

# declare a 2D empty list

b = [[0 for j in range(0,5)]for i in range(0, 4)]
print(b)
