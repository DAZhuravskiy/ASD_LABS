#Поразрядная
def _radix_nonneg(a):
    if not a:
        return a
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a:
            buckets[(x // exp) % 10].append(x)
        a = [x for bucket in buckets for x in bucket]
        exp *= 10
    return a


def radix_sort(a):
    if not a:
        return a
    negatives = _radix_nonneg([-x for x in a if x < 0])
    positives = _radix_nonneg([x for x in a if x >= 0])
    return [-x for x in reversed(negatives)] + positives


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:1 + n]
    print(*radix_sort(arr))
