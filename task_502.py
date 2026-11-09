number = input('Enter number: ')
result = []

for i in range(len(number)):
    num_number = number[:i] + number[i+1:]
    result.append(int(num_number))

print(max(result))