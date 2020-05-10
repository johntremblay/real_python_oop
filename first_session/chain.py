"""
Script that works with different classes
"""

class A:
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class X:
    def __init__(self):
        print('X')
        super().__init__()

class Forward(B, X):
    def __init__(self):
        print('Forward')
        super().__init__()

class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()

# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value “__main__”.
if __name__ == "__main__":
    forward = Forward()
else:
    print('Executed when imported')
