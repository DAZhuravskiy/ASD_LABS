import sys
import random


def quicksort(a):
    stack = [(0, len(a) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = a[random.randint(left, right)]
        i, j = left, right

        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        if left < j:
            stack.append((left, j))
        if i < right:
            stack.append((i, right))

    return a


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    arr = data[1:1 + n]

    print(*quicksort(arr))


if __name__ == "__main__":
    main()