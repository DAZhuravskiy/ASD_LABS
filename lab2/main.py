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

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b
    else:
        raise ValueError("Недопустимая операция.")

def get_precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    else:
        return 0

def evaluate_expression(expression):
    expr = expression.replace(' ', '')
    if not expr.endswith('='):
        return "Ошибка: выражение должно заканчиваться знаком '='."
    expr = expr[:-1]
    
    if not check_brackets(expr):
        return "Ошибка: неверное расположение скобок."
    
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit() or expr[i] == '.':
            num_str = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num_str += expr[i]
                i += 1
            tokens.append(float(num_str))
        elif expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        else:
            return f"Ошибка: недопустимый символ '{expr[i]}'."
    
    values = []
    ops = []
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if isinstance(token, float):
            values.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(calculate(op, val2, val1))
            ops.pop()
        else:
            if token == '-' and (i == 0 or (isinstance(tokens[i-1], str) and tokens[i-1] != ')')):
                values.append(0.0)
                
            while (ops and ops[-1] != '(' and 
                   get_precedence(ops[-1]) >= get_precedence(token)):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(calculate(op, val2, val1))
            ops.append(token)
        i += 1
        
    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(calculate(op, val2, val1))
        
    return values[0]

def main():
    user_input = input("Введите математическое выражение (например, 2+7*(3/9)-5=): ")
    try:
        result = evaluate_expression(user_input)
        if isinstance(result, str):
            print(result)
        else:
            if result.is_integer():
                print(f"Результат: {int(result)}")
            else:
                print(f"Результат: {result}")
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка при вычислении: {e}")

if __name__ == "__main__":
    main()
