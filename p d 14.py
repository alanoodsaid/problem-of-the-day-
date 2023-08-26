#Problemof the Day 14 
# Given string s representing a postfix expression, the task is to evaluat
# the expression and find the final value. operators will only 
# include the basic arthimatec operators like *, %, +,-
# input is S = "231* + 9-"
def evaluate_postfix(expression):
    stack = []

    operators = set(['+', '-','*', '/'])

    for char in expression:
        if char not in operators:
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()


            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
    return stack[0]

  # given input
S = "222* + 10-"
result = evaluate_postfix(S)
print("Result:", result)  
