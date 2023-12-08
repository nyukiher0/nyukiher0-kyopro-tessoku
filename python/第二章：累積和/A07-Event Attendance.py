"""
配列のインデックス範囲:
配列の長さを D+2 にすることで、R[i] が D（最終日）である場合でも、
R[i]+1 が配列の範囲外にならないようにしています。つまり、B[D+1] が存在することで、
最終日に終了するイベントの処理が可能になります。

累積和の計算:
Answer 配列は累積和を計算するために使用されます。
Answer[0] = 0 とし、1 から D+1 までの範囲で累積和を計算します。
この累積和によって、各日における総参加者数を効率的に求めることができます。
"""

D = int(input())
N = int(input())

S = [0] * (D+2)
ans = [0]

for i in range(N):
    L, R = map(int, input().split())
    S[L] += 1
    S[R+1] -= 1

for i in range(1,D+1):
    ans.append(ans[i-1] + S[i])

for i in range(1,D+1):
    print(ans[i])