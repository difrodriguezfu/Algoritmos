N = int(raw_input())
A = map(int, raw_input().split())

for i in range(N):
    temp = A[i]
    j = i
    while j > 0 and temp < A[j-1]:
        A[j] = A[j-1]
        j = j-1
    A[j] = temp

print A