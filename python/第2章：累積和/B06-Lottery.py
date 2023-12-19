N = int(input())
A = list(map(int,input().split()))
Q = int(input())
S = [0] * (N+1)

for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]

for _ in range(Q):
    L,R = map(int,input().split())

    hits = S[R] - S[L-1]

    if (R - (L - 1)) / 2 < hits:
        print("win")
    elif (R - (L - 1)) / 2 > hits:
        print("lose")
    else:
        print("draw")
