size, target = map(int, input().split())
counter = 0

for x in range(1, size + 1):
    if (target % x == 0) and (target / x <= size):
        counter += 1

print(counter)
