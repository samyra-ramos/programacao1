price=1000000
is_good_credit=True
discount=None

if is_good_credit:
    discount = price * 0.1
else:
    discount = price * 0.2
print(discount)
