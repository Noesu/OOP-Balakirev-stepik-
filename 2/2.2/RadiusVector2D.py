from typing import Union

class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, *args):
        self.__x, self.__y = 0, 0
        self.x = args[0] if len(args) > 0 else 0
        self.y = args[1] if len(args) > 1 else 0

    @property
    def x(self) -> Union[int, float]:
        return self.__x

    @x.setter
    def x(self, value: Union[int, float]) -> None:
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self) -> Union[int, float]:
        return self.__y

    @y.setter
    def y(self, value: Union[int, float]):
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        if isinstance(vector, RadiusVector2D):
            return pow(vector.x, 2) + pow(vector.y, 2)


########################################################################################################################

r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

assert hasattr(RadiusVector2D, 'MIN_COORD') and hasattr(RadiusVector2D, 'MAX_COORD'), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"

assert type(RadiusVector2D.x) == property and type(RadiusVector2D.y) == property, "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"

assert r1.x == 0 and r1.y == 0 and r2.x == 1 and r2.y == 0 and r3.x == 4 and r3.y == 5, "свойства x и y возвращают неверные значения"

assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"

r4 = RadiusVector2D(4.5, 5.5)
assert 4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6, "свойства x и y возвращают неверные значения"

r5 = RadiusVector2D(-102, 2000)
assert r5.x == 0 and r5.y == 0, "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

r = RadiusVector2D(10, 20)
r.x = 'a'
r.y = (1, 2)
assert r.x == 10 and r.y == 20, "присвоение не числовых значений должно игнорироваться"