"""
N 台のプリンターがあり、1 から N までの番号が付けられています。プリンター i は Ai 秒ごとにチラシを 1 枚印刷します。
すなわち、スイッチを入れてから Ai 秒後、2Ai 秒後、3Ai 秒後･･･ に印刷します。
すべてのプリンターのスイッチを同時に入れたとき、K 枚目のチラシが印刷されるのは何秒後でしょうか。
"""

left = 0
right = 10 ** 9

N, K = map(int, input().split())
A = list(map(int, input().split()))

while (left <= right):
    mid = (left + right) // 2
    
    papers = sum([mid // num for num in A])

    if papers < K:
        left = mid + 1
    else:
        right = mid - 1

print(left)
