#!/usr/bin/env python3

# Enhanced Python script to list functions in Python files in the current directory

import ast
import os

# Define visitor class to extract functions, following PEP8 naming conventions
class FunctionVisitor(ast.NodeVisitor):
    # Improved method documentation and naming
    def visit_FunctionDef(self, node):
        # 
        # Output function name and arguments using f-string for better readability
        # print(f"Function {node.name} {ast.unparse(node.args)} defined in {self.filename}")
        
        print(f"Function {node.name} defined in {self.filename}")
        print(f"docs: {ast.get_docstring(node)}")
        if node.returns:
            print(f"returns: {ast.unparse(node.returns)}")

        print(f"args: {ast.unparse(node.args)}")
        print(f"body: {ast.unparse(node.body)}")
        print(f"decorator_list: {ast.unparse(node.decorator_list)}")
        print()
        
        

# Initialize the visitor with the filename, which is needed for the output
for filename in os.listdir('.'):
    if filename.endswith('.py'):
        with open(filename, 'r', encoding='utf-8') as file:
            # Parse the AST tree from the file's content
            tree = ast.parse(file.read(), filename=filename)
            # Create a new visitor instance and visit the AST
            visitor = FunctionVisitor()
            visitor.filename = filename