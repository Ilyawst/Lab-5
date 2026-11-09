a = input().replace(',', '').split()
b = input().replace(',', '').split()

result = []
for i in a:
    if (i in b) and (i not in result):
        result.append(i)

print(' '.join(result))
