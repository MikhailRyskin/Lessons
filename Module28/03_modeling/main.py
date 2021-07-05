from shapes import Square, Triangle, Cube, Pyramid


square_1 = Square(length=5)
print(square_1.square_per(), square_1.square_sq())
square_1.length = 7.87
print(square_1.square_per(), square_1.square_sq())

triangle_1 = Triangle(length=4, height=6)
print(triangle_1.triangle_sq())
triangle_1.length = 8
triangle_1.height = 7
print(triangle_1.triangle_sq())

cube_1 = Cube(length=8)
print(cube_1.cube_sq())

pyramid_1 = Pyramid(length=6, height=10)
print(pyramid_1.pyramid_sq())
