list = [int(i) for i in input().split()]
k = int(input())

n = len(list)
k = k % n

list[:] = list[-k:] + list[:-k]

print(' '.join([str(i) for i in list]))
