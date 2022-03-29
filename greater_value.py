num = input()
num1 = num.split(' ')
A=int(num1[0])
B=int(num1[1])
C=int(num1[2])
D=int(num1[3])

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and (A % 2) == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')