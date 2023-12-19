# しゃくとり法
# N, K = map(int,input().split())
# A = list(map(int,input().split()))

# R = [None] * N

# for i in range(len(A)-1):
#     # 右側 idx のスタート地点を決める
#     if i == 0:
#         R[i] = 0
#     else:
#         R[i] = R[i-1]
    
#     while(R[i] < N-1 and A[R[i]+1]-A[i] <= K):
#         R[i] += 1

# ans = 0
# for i in range(len(A)-1):
#     ans += (R[i] - i)

# print(ans)

# 二分探索法
N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N

for i in range(len(A) - 1):
    l, r = i, len(A) - 1
    while(l <= r):
        mid = (l + r) // 2
        if A[mid] - A[i] <= K:
            l = mid + 1
        else:
            r = mid - 1
    R[i] = r

ans = 0
for i in range(N - 1):
    ans += R[i] - i

print(ans)


