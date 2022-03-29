N = int(input())
bills = [100,50,20,10,5,2,1]
print(N)
index=0
while index < len(bills):
    bill = bills[index]
    num_notes = 0
    if N - bill >= 0:
        num_notes = int(N / bill)
        N = N % bill
    print(f'{num_notes} nota(s) de R$ {bill},00')
    

    index = index + 1
