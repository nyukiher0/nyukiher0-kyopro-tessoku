N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0]

for i in range(len(A)):
    S.append(S[i] + A[i])

for i in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L-1])
