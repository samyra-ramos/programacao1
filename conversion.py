weight=input('Weight:')
print(weight)
unit=input('(L)bs or (K)g:')
print(unit)

if unit.lower() == 'l':
    weight = float(weight) * 0.45
    message = f'You are {weight} kilos'
elif unit.lower() == 'k':
    weight = float(weight) * 2.205
    message = f'You are {weight} pounds'
else:
    message = 'please choose correct unit'

print(message)