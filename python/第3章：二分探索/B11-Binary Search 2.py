# bisectモジュールを使って解く
# import bisect

# N = int(input())
# A = list(map(int,input().split()))

# sorted_A = sorted(A)

# Q = int(input())

# for i in range(Q):
#     X = int(input())
#     pos = bisect.bisect_left(sorted_A, X)
#     if pos < len(A) - 1 and sorted_A[pos] == X:
#         pos = bisect.bisect_left(sorted_A, (X-1))
#         print(pos)
#     else:
#         print(pos)

# めぐる式二分探索法で解く
def validate(sorted_array, target, mid):
    if sorted_array[mid] < target:
        return True
    else:
        return False

N = int(input())
A = list(map(int,input().split()))

sorted_A = sorted(A)
Q = int(input())

for i in range(Q):
    X = int(input())
    ok = - 1
    ng = len(A)
    while(abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if validate(sorted_A, X, mid):
            ok = mid
        else:
            ng = mid
    print(ok + 1)