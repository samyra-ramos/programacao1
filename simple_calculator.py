product_1 = input()
product_2 = input()

product_1_numbers = product_1.split(' ')
product_2_numbers = product_2.split(' ')

total_product_1 = int(product_1_numbers[1]) * float(product_1_numbers[2])
total_product_2 = int(product_2_numbers[1]) * float(product_2_numbers[2])

print(f'VALOR A PAGAR: R$ {format(total_product_1 + total_product_2, ".2f")}')

