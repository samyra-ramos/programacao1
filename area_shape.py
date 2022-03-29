data = input()
numbers = data.split(' ')
a_base = numbers[0]
b_base = numbers[1]
c_height = numbers[2]

pi = 3.14159
area_triangle = float(a_base) * float(c_height)/2
area_circle = pi * float(c_height) **2
area_trapezium = (1/2) * (float(a_base) + float(b_base)) * float(c_height)
area_square = float(b_base) **2
area_rectangle = float(a_base) * float(b_base)

print(f'TRIANGULO: {format(area_triangle, ".3f")}')
print(f'CIRCULO: {format(area_circle, ".3f")}')
print(f'TRAPEZIO: {format(area_trapezium, ".3f")}')
print(f'QUADRADO: {format(area_square, ".3f")}')
print(f'RETANGULO: {format(area_rectangle, ".3f")}')