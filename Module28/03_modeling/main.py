from shapes1 import Square, Triangle, Cube, Pyramid

square_1 = Square(length=5)
print(square_1.get_perimeter(), square_1.get_square())
square_1.length = 7.87
print(square_1.get_perimeter(), square_1.get_square())

triangle_1 = Triangle(length=4, height=6)
print(triangle_1.get_square())
triangle_1.length = 8
triangle_1.height = 7
print(triangle_1.get_square())

cube_1 = Cube(length=8)
print(cube_1.total_square())

pyramid_1 = Pyramid(length=6, height=10)
print(pyramid_1.total_square())

# зачёт!
