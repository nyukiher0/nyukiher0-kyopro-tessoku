H,W,N = map(int,input().split())

# 累積和を取得する過程で、（C,D）の外側（C+1,D+1）にアクセスするため、HxWについて始めと終わりの余白が必要
S = [[0 for _ in range(W+2)] for _ in range(H+2)]

for i in range(N):
    A,B,C,D = map(int,input().split())
    S[A][B] += 1
    S[A][D+1] -= 1
    S[C+1][B] -= 1
    S[C+1][D+1] += 1

# 横方向の累積和
for i in range(1,H+2):
    for j in range(1,W+2):
        S[i][j] += S[i-1][j]

# 縦方向の累積和
for i in range(1,H+2):
    for j in range(1,W+2):
        S[i][j] += S[i][j-1]

# 出力結果のフォーマット
formatted_result = ""
for row in S[1:-1]:
    formatted_row = " ".join(map(str, row[1:-1]))
    formatted_result += formatted_row + "\n"

print(formatted_result)