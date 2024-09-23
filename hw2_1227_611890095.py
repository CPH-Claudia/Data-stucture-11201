# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:17:05 2023

@author: user
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
    
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def is_operator(char):
    return char in ['+', '-', '*', '/']

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    postfix = []
    for char in expression:
        if char.isdigit():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while not stack.is_empty() and precedence[char] <= precedence.get(stack.peek(), 0):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)

def construct_expression_tree(postfix):
    stack = Stack()
    for char in postfix:
        if char.isdigit():
            node = Node(char)
            stack.push(node)
        elif is_operator(char):
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.push(node)
    return stack.pop()

def evaluate_expression_tree(root):
    if root:
        left = evaluate_expression_tree(root.left)
        right = evaluate_expression_tree(root.right)

        if root.value.isdigit():
            return int(root.value)
        else:
            if root.value == '+':
                return left + right
            elif root.value == '-':
                return left - right
            elif root.value == '*':
                return left * right
            elif root.value == '/':
                return left / right  # For Python 3, this will give a float result

def infix_to_answer(expression):
    postfix = infix_to_postfix(expression)
    print(f'後序運算式(Postfix): {postfix}')
    tree = construct_expression_tree(postfix)
    result = evaluate_expression_tree(tree)
    return result

# 使用範例
infix_expression = "2*(8+7)-9/3"
answer = infix_to_answer(infix_expression)
print(f'計算結果: {answer}')