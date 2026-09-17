def is_valid_number(n):
    temp = n
    while temp % 3 == 0:
        temp //= 3
    while temp % 5 == 0:
        temp //= 5
    while temp % 7 == 0:
        temp //= 7
    
    return temp == 1

def main():
    try:
        x = int(input("Введите число x: "))
        if x < 1:
            print("Число должно быть больше 0.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    result = []
    for i in range(1, x + 1):
        if is_valid_number(i):
            result.append(i)
            
    print(f"Числа от 1 до {x}, удовлетворяющие условию (3^K * 5^L * 7^M):")
    print(result)

if __name__ == "__main__":
    main()