H, W = map(int, input().split())
X = []
S = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(H):
    X.append(list(map(int,input().split())))

# 横方向の累積和を考える
for i in range(1,H+1):
    for j in range(1,W+1):
        S[i][j] = S[i][j-1] + X[i-1][j-1]

# 縦方向の累積和を考える
for i in range(1,H+1):
    for j in range(1,W+1):
        S[i][j] += S[i-1][j]

Q = int(input())

for i in range(Q):
    A,B,C,D = map(int,input().split())
    print(S[C][D]+S[A-1][B-1]-S[A-1][D]-S[C][B-1])
