N = float(input())
bills = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
index = 0
while index < len(bills):
    bill = bills[index]
    num_notes = 0
    if N - bill >= 0:
        num_notes = int(N/ bill)
        N = N % bill

    if bill > 1:
        money = 'nota'
    else:
        money = 'moeda'
    
    if index == 0:
        print('NOTAS:')

    if index == 6:
        print('MOEDAS:')
    
    print(f'{num_notes} {money}(s) de R$ {format(bill, ".2f")}')
    index = index + 1



