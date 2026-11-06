import sys

RUN_SIZE = 3


def merge_lists(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


def valid_distribution(a, b):
    state = [a, b, 0]

    while True:
        nonempty = [i for i, x in enumerate(state) if x > 0]

        if len(nonempty) == 1:
            return state[nonempty[0]] == 1

        if len(nonempty) != 2:
            return False

        empty = [i for i in range(3) if state[i] == 0][0]
        i, j = nonempty
        m = min(state[i], state[j])

        state[i] -= m
        state[j] -= m
        state[empty] = m


def find_distribution(runs_count):
    for a in range(1, runs_count):
        b = runs_count - a
        if valid_distribution(a, b):
            return a, b
    raise RuntimeError("Не удалось подобрать распределение серий")


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    arr = data[1:1 + n]

    if n == 0:
        print()
        return

    runs = []
    for i in range(0, n, RUN_SIZE):
        chunk = arr[i:i + RUN_SIZE]
        chunk.sort()
        runs.append(chunk)

    r = len(runs)

    if r == 1:
        print(*runs[0])
        return

    a, b = find_distribution(r)
    files = [runs[:a], runs[a:a + b], []]

    while True:
        total_runs = sum(len(f) for f in files)

        if total_runs == 1:
            for f in files:
                if f:
                    print(*f[0])
                    return

        nonempty = [i for i, f in enumerate(files) if f]
        empty = [i for i in range(3) if not files[i]]

        if len(nonempty) != 2 or len(empty) != 1:
            flat = [x for f in files for run in f for x in run]
            flat.sort()
            print(*flat)
            return

        i, j = nonempty
        e = empty[0]

        m = min(len(files[i]), len(files[j]))

        for _ in range(m):
            left = files[i].pop(0)
            right = files[j].pop(0)
            files[e].append(merge_lists(left, right))


if __name__ == "__main__":
    main()