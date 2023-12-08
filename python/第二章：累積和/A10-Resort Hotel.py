N = int(input())
A = list(map(int,input().split()))

max_left = [0] * (N+1)
max_right = [0] * (N+1)

for i in range(N):
    max_left[i+1] = max(max_left[i],A[i])

for i in range(N-1,-1,-1):
    max_right[i] = max(max_right[i+1],A[i])

D = int(input())
for _ in range(D):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    print(max(max_left[l],max_right[r+1]))