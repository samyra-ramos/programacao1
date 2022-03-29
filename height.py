altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

imc = peso/(altura**2)
imc = round(imc,2)

print(f'O IMC é:{imc}')
if imc < 18.5: 
    print('Magreza')
elif imc >= 18.5 and imc<= 24.99:
    print('Normal')
elif imc >= 25 and imc<= 29.99:
    print('Sobrepeso')
elif imc >= 30 and imc<= 39.99:
    print('Obesidade')
else: 
    print('Obesidade Grave')

