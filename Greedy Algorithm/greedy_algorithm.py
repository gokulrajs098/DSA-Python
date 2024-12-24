coins = [1, 2, 5]
amount = 8
coins.sort(reverse=True)

count = 0

for coin in coins:
    count += amount//coin
    amount = amount%coin
print(count)