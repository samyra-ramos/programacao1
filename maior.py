data = input()
numbers = data.split(' ')

def maior_xy(x, y):
    return (int(x) + int(y) + abs(int(x) - int(y)))/2

if len(numbers) > 1:
    maior = maior_xy(numbers[0], numbers[1])

    i = 2
    while i < len(numbers):
        maior = maior_xy(maior, numbers[i])
        i = i + 1

elif len(numbers) == 1:
    maior = numbers[0]
else:
    maior = None


print(f'{maior} eh o maior')
