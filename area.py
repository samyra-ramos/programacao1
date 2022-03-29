values = (input())
area_values = values.split(' ')
A = float(area_values[0])
B = float(area_values[1])
C = float(area_values[2])

pi = 3.14159

area_triangle = (A * C)/2
area_circle = pi * (C**2)
area_trapezium = ((A + B) * C)/2
area_square = B * B
area_rectangle_2 = A * B

print(f'TRIANGULO: {format(area_triangle, ".3f")}')
print(f'CIRCULO: {format(area_circle, ".3f")}')
print(f'TRAPEZIO: {format(area_trapezium, ".3f")}')
print(f'QUADRADO: {format(area_square, ".3f")}')
print(f'RETANGULO: {format(area_rectangle_2, ".3f")}')



