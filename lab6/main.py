#Выбором
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n = data[0]
    arr = data[1:1 + n]
    print(*selection_sort(arr))
