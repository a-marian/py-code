"""
/**
  150. Evaluate Reverse Polish Notation
  Evaluate the value of an arithmetic expression in Reverse Polish Notation.
  Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
  Note that division between two integers should truncate toward zero.
  It is guaranteed that the given RPN expression is always valid. That means the expression
  would always evaluate to a result, and there will not be any division by zero operation.
  Example
  Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  Output: 22
  Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
 * */
"""


def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif c == "*":
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(c))
    return stack[0]


tokens = List["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
