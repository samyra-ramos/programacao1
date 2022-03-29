age = int(input())
year = age // 365
if year > 0:
    print(f'{year} ano(s)')
    age = age % 365
else:
    print(f'{year} ano(s)')

months = age // 30
if months > 0:
    print(f'{months} mes(es)')
    age = age % 30
else: 
    print(f'{months} mes(es)')

days = age 
print(f'{days} dia(s)') 
