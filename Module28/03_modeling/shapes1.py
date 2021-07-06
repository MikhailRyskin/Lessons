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

    def get_perimeter(self) -> float:
        self.perimeter = self._length * 4
        return self.perimeter

    def get_square(self) -> float:
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

    def get_perimeter(self) -> float:
        self.perimeter = math.sqrt((self._length / 2) ** 2 + self._height ** 2) * 2 + self._length
        return self.perimeter

    def get_square(self) -> float:
        self.square = self._length * self._height / 2
        return self.square


class MixSquare:
    """
    Класс - миксин. Метод позволяет вычислять общую площадь 3D фигуры
    по сумме площадей входящих в неё 2D фигур.
    """
    def total_square(self) -> float:
        square_total = 0
        for elem in self.figure:
            square_total += elem.get_square()
        return square_total


class Cube(Square, MixSquare):
    """
    Класс, описывающий куб. Задаётся стороной куба.
    Методы позволяют вычислять площадь.
    """
    def __init__(self, length: float) -> None:
        super().__init__(length=length)
        self.figure = [Square(self.length)] * 6


class Pyramid(Triangle, Square, MixSquare):
    """
    Класс, описывающий пирамиду. Задаётся длиной основания и высотой.
    Методы позволяют вычислять площадь.
    """
    def __init__(self, length: float, height: float) -> None:
        super().__init__(length=length, height=height)
        self.figure = [Triangle(self._length, self._height)] * 4
        self.figure.append(Square(self.length))
