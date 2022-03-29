N = int(input())
hour = N // 3600
if hour > 0:
    N = N % 3600

minute = N // 60
if minute > 0:
    N = N % 60

second = N  
print(f'{hour}:{minute}:{second}')
