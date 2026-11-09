n = input().split()
numbers = [int(i) for i in n]

max_number = max(numbers)
index = numbers.index(max_number)

print(max_number, index)
