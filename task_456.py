items = input().split(',')

result = []
for i in items:
    number = int(i, 2)
    if number % 5 == 0:
        result.append(i)

print(','.join(result))
