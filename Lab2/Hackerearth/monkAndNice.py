N = int(raw_input())
A = []

for i in range(N):
    A.append(raw_input())

sum = 0
for i in range(N):
    temp = A[i]
    for j in range(i):
        if A[j] < temp:
            sum += 1
    print sum
    sum = 0