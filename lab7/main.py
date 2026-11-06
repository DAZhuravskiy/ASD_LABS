def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = a[i]
            j = i
            while j >= gap and a[j - gap] > tmp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = tmp
        gap //= 2
    return a


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:1 + n]
    print(*shell_sort(arr))