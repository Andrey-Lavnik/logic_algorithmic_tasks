from math import floor

gold = int(input())
prices = list(map(int, input().split()))
min_price = min(prices)
if gold < min_price:
    print("-1")
    exit()

last_index = len(prices) - prices[::-1].index(min_price) - 1
valuable_number = last_index + 1
number_of_digits = floor(gold / min_price)
spent_gold = min_price * number_of_digits
current_label = str(valuable_number) * number_of_digits
rest_of_gold = gold - spent_gold

if rest_of_gold == 0:
    print(current_label)
    exit()

while rest_of_gold != 0:
    rest_of_gold += min_price
    current_label = current_label[:-1]
    available_numbers = []

    for p in prices:
        if min_price <= p <= rest_of_gold:
            number = len(prices) - prices[::-1].index(p)
            available_numbers.append(number)
    if len(available_numbers) == 0:
        exit()

    additional_number = max(available_numbers)
    current_label = str(additional_number) + str(current_label)
    rest_of_gold -= prices[additional_number - 1]

    if additional_number == valuable_number:
        break

print(current_label)