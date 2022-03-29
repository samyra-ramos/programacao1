numero = int(input('Digite um número inteiro menor que 1000: '))
result = ''
centena = numero // 100
print(centena)
numero = numero - (centena * 100) 
dezena = numero/ 10 
unidade = numero % 10 

if centena == 1:
  result = '1 centena'
elif centena > 1:
  result = str(centena) + 'centenas'


if dezena == 1: 
  result = result + '1 dezena'
elif dezena > 1:
  result = result + str(dezena) + ', dezenas'

if unidade == 1: 
  result = result + str(unidade) + 'unidade'
elif unidade > 1: 
  result = result + str(unidade) + 'e unidades.'

print(result)