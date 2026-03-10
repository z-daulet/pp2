from functools import reduce

n= [1,2,3,4,5]
total = reduce(lambda x,y: x+y, n)
print(total)

transactions = [50, 120, 250, 30, 400, 85, 110]

high_value_transactions = filter(lambda x: x > 100, transactions)

taxed_transactions = map(lambda x: x * 1.1, high_value_transactions)

print(list(taxed_transactions))

