N = int(input())
XY = []


for _ in range(N):
    X,Y = map(int, input().split())
    XY.append([X,Y])

X_MAX = max([X for [X, Y] in XY])
Y_MAX = max([Y for [X, Y] in XY])

XYMAP = [[0 for _ in range(Y_MAX + 1)] for _ in range(X_MAX + 1)]

for [X, Y] in XY:
    XYMAP[X][Y] += 1

for i in range(1,X_MAX+1):
    for j in range(1,Y_MAX+1):
        XYMAP[i][j] += XYMAP[i][j-1]

for i in range(1,X_MAX+1):
    for j in range(1,Y_MAX+1):
        XYMAP[i][j] += XYMAP[i-1][j]

Q = int(input())

for i in range(Q):
    a,b,c,d = map(int, input().split())
    print(XYMAP[c][d] + XYMAP[a-1][b-1] - XYMAP[a-1][d] - XYMAP[c][b-1])
