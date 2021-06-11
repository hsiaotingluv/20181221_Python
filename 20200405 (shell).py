Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp = ('hsiaoting', 'zhenghong', 'hsiaohong', 'hsiaotong')
>>> type(temp)
<class 'tuple'>
>>> temp = temp[:2] + ('hsiaohsiao', ) + temp[2:]
>>> temp
('hsiaoting', 'zhenghong', 'hsiaohsiao', 'hsiaohong', 'hsiaotong')
>>> del temp
>>> temp
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    temp
NameError: name 'temp' is not defined
>>> 