Объявите класс с именем **Triangle**, объекты которого создаются командой:

`tr = Triangle(a, b, c)`

где _a, b, c_ - длины сторон треугольника (числа: целые или вещественные). В классе **Triangle** объявите следующие дескрипторы данных:

_a, b, c_ - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:

`raise ValueError("длины сторон треугольника должны быть положительными числами")`

Также нужно проверять, что все три стороны _a, b, c_ могут образовывать стороны треугольника. То есть, должны выполняться условия:
```python
a < b+c; b < a+c; c < a+b
```
Иначе генерируется исключение командой:
```python
raise ValueError("с указанными длинами нельзя образовать треугольник")
```
Наконец, с объектами класса **Triangle** должны выполняться функции:

_len(tr)_ - возвращает периметр треугольника, приведенный к целому значению с помощью функции _int()_;  
_tr()_ - возвращает площадь треугольника (можно вычислить по формуле Герона: `s = sqrt(p * (p-a) * (p-b) * (p-c))`, где _p_ - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс **Triangle**.