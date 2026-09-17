def check_brackets(string):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

def main():
    input_string = input("Введите строку: ")

    if check_brackets(input_string):
        print("Скобки расставлены корректно.")
    else:
        print("Скобки расставлены некорректно.")

if __name__ == "__main__":
    main()