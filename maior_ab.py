maior_AB = input()
number_maiorAB = maior_AB.split(' ')
A = int(number_maiorAB[0])
B = int(number_maiorAB[1])
C = int(number_maiorAB[2])

result_maiorab = (A + B + abs(A - B))/2
maior = (result_maiorab + C + abs(result_maiorab - C))/2
print(f'{maior} eh o maior')