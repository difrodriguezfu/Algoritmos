N = int(raw_input())
A = map(int, raw_input().split())
    
step = 0
for j in range(N-1):
    for i in range(N-j-1):
        #print A[i], A[i+1]
        #print A[i] > A[i+1]

        #print A
        if A[i] > A[i+1]:
            step += 1
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            
# print A
print step