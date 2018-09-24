N = int(raw_input())
A = map(int, raw_input().split())

for i in range(N):
    temp = A[i]
    j = i
    while j > 0 and temp < A[j-1]:
        A[j] = A[j-1]
        j = j-1
    A[j] = temp
Z = []
V = []
for i in range(N):
    if A[i] % 2 == 0:
        Z.append(A[i])
    else:
        V.append(A[i])

for i in range(len(Z)):
    print Z[i],
print sum(Z),
for i in range(len(V)):
    print V[i],
print sum(V)
