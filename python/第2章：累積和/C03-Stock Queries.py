D = int(input())
X = int(input())
A = []
S = [0] * D
S[0] = X

for i in range(D-1):
    A.append(int(input()))

for i in range(1,D):
    S[i] = S[i-1] + A[i-1]

Q = int(input())

for i in range(Q):
    L,R = map(int, input().split())
    if S[L-1] > S[R-1]:
        print(L)
    elif S[L-1] < S[R-1]:
        print(R)
    else:
        print("Same")
