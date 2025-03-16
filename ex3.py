import sys
import operator

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(tokens):
    stack = []
    ops = []
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    def process_op():
        op = ops.pop()
        right = stack.pop()
        left = stack.pop()
        node = Node(op)
        node.left = left
        node.right = right
        stack.append(node)
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit():
            stack.append(Node(int(token)))
        elif token in precedence:
            while ops and precedence[ops[-1]] >= precedence[token]:
                process_op()
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                process_op()
            ops.pop()
        i += 1
    
    while ops:
        process_op()
    
    return stack[0]

def evaluate_tree(node):
    if isinstance(node.value, int):
        return node.value
    
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    return operations[node.value](left_val, right_val)

def parse_expression(expression):
    tokens = []
    num = ""
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if char in "()+-*/":
                tokens.append(char)
    if num:
        tokens.append(num)
    return tokens

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex3.py \"expression\"")
        sys.exit(1)
    
    expression = sys.argv[1]
    tokens = parse_expression(expression)
    tree = build_tree(tokens)
    result = evaluate_tree(tree)
    print(result)
