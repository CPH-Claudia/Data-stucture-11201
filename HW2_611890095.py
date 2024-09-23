# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:01:04 2023

@author: user
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def build_expression_tree(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def is_operator(op):
        return op in precedence

    def build_tree_from_infix(exp):
        stack = []
        root = None
        for char in exp:
            if char.isdigit():
                node = Node(char)
                stack.append(node)
            elif is_operator(char):
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        if stack:
            root = stack.pop()
        return root

    return build_tree_from_infix(expression)

# 建立後序運算式
def postfix_expression(root):
    if root:
        left = postfix_expression(root.left)
        right = postfix_expression(root.right)
        return left + right + root.value
    return ''

def evaluate_postfix_expression(postfix):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
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

    return stack.pop()

# 測試程式碼
infix_expression = "2*(8+7)-9/3"
root = build_expression_tree(infix_expression)
postfix = postfix_expression(root)
print(f"後序運算式(Postfix): {postfix}")
result = evaluate_postfix_expression(postfix)
print(f"計算結果: {result}")