product_1 = input()
product_2 = input()

product_1_values = product_1.split(' ')
product_2_values = product_2.split(' ')

total_product_1 = int(product_1_values[1]) * float(product_1_values[2])
total_product_2 = int(product_2_values[1]) * float(product_2_values[2])

print(f'VALOR A PAGAR: R$ {format(total_product_1 + total_product_2, ".2f")}')