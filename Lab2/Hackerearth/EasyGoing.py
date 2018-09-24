T = int(raw_input())

for k in range(T):
    N,M = map(int,raw_input().split())
    A = map(int, raw_input().split())

    for j in range(N-1):
        for i in range(N-j-1):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

    dif = N - M
    sum1 = 0
    sum2 = 0

    for i in range(dif):
        sum1 += A[i]

    for j in reversed(range(N-dif, N)):
        sum2 += A[j]
    
    print sum2 - sum1