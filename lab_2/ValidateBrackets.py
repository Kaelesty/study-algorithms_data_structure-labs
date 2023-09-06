"""
напишите функцию проверяющую корректность скобочной последовательности в строке,
состоящей из скобок следующего типа - (, {, [, ], }, ).
Необходимо проверить, является ли скобочная последовательность корректной,
то есть количество открывающих скобок равно количеству закрывающих,
и при этом на каждой позиции закрывающая скобка имеет соответствующую открывающую скобку.
"""


from MyStack import MyStack

def validate_brackets(string: str) -> bool:

    bracket_pairs: dict[str, str] = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    stack: MyStack[str] = MyStack()

    for char in string:
        if char in bracket_pairs.keys():
            stack.push(char)
        elif char in bracket_pairs.values():
            if stack.empty():
                return False
            previous_char: str = stack.pop()
            if bracket_pairs[previous_char] != char:
                return False
        else:
            raise RuntimeError(f"Unknown symbol: {char}")
    return stack.empty()

