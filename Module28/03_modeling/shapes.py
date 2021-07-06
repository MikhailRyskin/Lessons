import math


class Square:
    """
    Класс, описывающий квадрат. Задаётся стороной квадрата.
    Методы позволяют вычислять периметр и площадь.
    """

    def __init__(self, length: float) -> None:
        self._length = length
        self.square = 0
        self.perimeter = 0

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        self._length = length

    def square_per(self) -> float:
        self.perimeter = self._length * 4
        return self.perimeter

    def square_sq(self) -> float:
        self.square = self._length ** 2
        return self.square


class Triangle:
    """
    Класс, описывающий треугольник. Задаётся длиной основания и высотой.
    Методы позволяют вычислять периметр и площадь.
    """

    def __init__(self, length: float, height: float) -> None:
        self._length = length
        self._height = height
        self.square = 0
        self.perimeter = 0

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        self._length = length

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height

    def triangle_per(self) -> float:
        self.perimeter = math.sqrt((self._length / 2) ** 2 + self._height ** 2) * 2 + self._length
        return self.perimeter

    def triangle_sq(self) -> float:
        self.square = self._length * self._height / 2
        return self.square



class Cube(Square):
    """
    Класс, описывающий куб. Задаётся стороной куба.
    Методы позволяют вычислять площадь.
    """

    def cube_sq(self) -> float:
        super().square_sq()
        self.square *= 6
        return self.square


class Pyramid(Triangle, Square):
    """
    Класс, описывающий пирамиду. Задаётся длиной основания и высотой.
    Методы позволяют вычислять площадь.
    """

    def pyramid_sq(self) -> float:
        super().triangle_sq()
        self.square *= 4
        temp = self.square
        super().square_sq()
        self.square += temp
        return self.square

#  предлагаю попробовать добавить в решение класс Миксин
#  с одним методом - расчётом площади фигуры.
#  предлагаю у каждой двумерной фигуры описать метод для расчёта её площади.
#  Методы стоит назвать одинаково. У каждой трёх мерной фигуры стоит создать аргумент - список двухмерных фигур.
#  В таком случае, в классе Миксин, необходимо просто пройти в цикле по списку фигур и получить сумму их площадей.
#  Главное, чтобы методы двухмерных и трёхмерных фигур назывались одинаково.
