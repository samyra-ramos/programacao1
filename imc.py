weight = float(input('Weight(kg):'))
height = float(input('Height(cm):'))
imc = weight / (height/100)**2


if imc < 18.5: 
    print(f'Seu IMC é {imc}, magreza')
elif imc >= 18.5 and imc < 24.9:
    print(f'Seu IMC é {imc}, normal')
elif imc >= 25 and imc < 29.9:
    print(f'Seu IMC é {imc}, sobrepeso')
else:
    print(f'Seu IMC é {imc},Obesidade')





