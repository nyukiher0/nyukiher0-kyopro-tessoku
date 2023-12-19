"""
問題文
小さい順に並べられている、要素数 N の配列 A=[A1,A2,⋯,AN] があります。要素 X は配列 A の何番目に存在するかを出力してください。
なお、この問題は単純な全探索（→1.2節）でも解けますが、ここでは二分探索法を使って実装してください。

制約
1≤N≤100000
1≤A1<A2<⋯<AN≤10^9
 整数 X は A1,A2,…,ANのいずれかである
"""

N, X = map(int, input().split())
A = list(map(int,input().split()))

left = 0
right = len(A) - 1
ans = 0

while(left <= right): # (left < right) だとWAとなる。=を含めるのが一般的な理由は以下。
    mid = (left + right) // 2

    if A[mid] > X:
        right = mid - 1
    elif A[mid] == X:
        ans = mid + 1
        break
    if A[mid] < X:
        left = mid + 1

print(ans)

"""
left < right の問題
left < right を条件とした場合、配列の要素が2つだけ残った状況で問題が発生します。
この時、left と right は隣接しているため、mid は常に left と同じ値になります。

もし A[mid] が X より小さい場合、left は mid + 1 に更新され、left と right が等しくなります。
この時、left < right が偽となり、ループが終了しますが、実際には right に位置する要素をチェックせずに終了してしまうため、
要素が見つかっていない可能性があります。
"""