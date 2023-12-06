N = int(input())

# 鉄則本の意図とは異なるコーディングです。
# 覚えやすいコーディングであれば問題ないと判断します。
bin_N = bin(N)
bin_N = bin_N[2:]

print("{:>010}".format(str(bin_N)))