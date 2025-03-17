#CREATE A TREE AND EVALUATE MATHEMATICAL EXPRESSION 
import sys
import operator

class Node: #node in the expreion tree
    def __init__(self, value):
        self.value = value #int or operand 
        self.left = None #child node
        self.right = None #child node

def build_tree(tokens): #
    stack = [] #stores nodes
    ops = [] #stores operators 
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2} #BEDMAS
    
    def process_op(): 
        op = ops.pop()
        right = stack.pop() #pops top operator and 2 operands
        left = stack.pop()
        node = Node(op) #new node
        node.left = left #attaches operands 
        node.right = right
        stack.append(node) #pushes the subtree to stack
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit():
            stack.append(Node(int(token))) #numbers to nodes
        elif token in precedence:
            while ops and precedence[ops[-1]] >= precedence[token]:
                process_op() #process higher/equal precedence operators
            ops.append(token)
        elif token == '(':
            ops.append(token) #stores brackets
        elif token == ')':
            while ops and ops[-1] != '(':
                process_op() #process until bracket is found
            ops.pop() #remove bracket
        i += 1
    
    while ops:
        process_op() #process remaining operators to coplete tree
    
    return stack[0]

def evaluate_tree(node):
    if isinstance(node.value, int): #node.value==int then return
        return node.value
    
    #recursively evaluate left and rigt subtree 
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    return operations[node.value](left_val, right_val)

def parse_expression(expression): #converts the expresion into tokens and handle multi-digits numbers properly
    # stores operands and operators together in brackets
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

#runs the program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex3.py \"expression\"")
        sys.exit(1)
    
    expression = sys.argv[1] #reas expression
    tokens = parse_expression(expression) # parse into tokens
    tree = build_tree(tokens) #build tree
    result = evaluate_tree(tree) #evaluate 
    print(result)
