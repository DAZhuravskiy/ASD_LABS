def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr

def main():
    try:
        input_str = input("Введите числа через пробел: ")
        arr = [float(x) for x in input_str.split()]
        
        if len(arr) == 0:
            print("Ошибка: массив пуст.")
            return
            
        print(f"Исходный массив: {arr}")
        sorted_arr = insertion_sort(arr)
        print(f"Отсортированный массив: {sorted_arr}")
        
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    main()