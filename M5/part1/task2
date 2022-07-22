class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

p1 = Point(2, 2)
p2 = Point(4, 4)
p3 = p1 + p2
p4 = p1 - p2
print(f'p1: ({p1.x}, {p1.y})')
print(f'p2: ({p2.x}, {p2.y})')
print(f'Сумма: ({p3.x}, {p3.y})')
print(f'Разность: ({p4.x}, {p4.y})')