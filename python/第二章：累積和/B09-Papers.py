N = int(input())

ans = 0

# XYMAP の最大サイズを確定する
X_MAX = 0
Y_MAX = 0

XYMAP = [[0 for _ in range(1501)] for _ in range(1501)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    # 最大の X, Y 座標を更新
    X_MAX = max(X_MAX, C)
    Y_MAX = max(Y_MAX, D)
    # 各紙の座標に対して更新
    XYMAP[A][B] += 1
    XYMAP[C][B] -= 1
    XYMAP[A][D] -= 1
    XYMAP[C][D] += 1

# 累積和の計算
for i in range(1, X_MAX+1):
    for j in range(1, Y_MAX+1):
        XYMAP[i][j] += XYMAP[i][j-1]

for i in range(1, X_MAX+1):
    for j in range(1, Y_MAX+1):
        XYMAP[i][j] += XYMAP[i-1][j]

# 重なる紙の面積を計算
ans = 0
for i in range(1, X_MAX):
    for j in range(1, Y_MAX):
        if XYMAP[i][j] > 0:
            ans += 1

print(ans)