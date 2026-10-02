def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr

def main():
    try:
        input_str = input("Введите числа через пробел: ")
        arr = [float(x) for x in input_str.split()]
        
        if len(arr) == 0:
            print("Ошибка: массив пуст.")
            return
            
        print(f"Исходный массив: {arr}")
        sorted_arr = comb_sort(arr)
        print(f"Отсортированный массив: {sorted_arr}")
        
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    main()