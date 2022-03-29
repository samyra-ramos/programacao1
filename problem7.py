number = input()
hours = input()
salary_hour = input()
currency= input()
SALARY = int(hours) * float(salary_hour)
symbol = 'U$'

if currency.lower() == 'real':
    symbol = 'R$'


print(f'NUMBER = {number}')
print(f'SALARY = {symbol} {format(SALARY, ".2f")}')
