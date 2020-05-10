"""
My main file
"""
from shapes import Square

class Square:
    pass


# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value “__main__”.
if __name__ == "__main__":


else:
    print('Executed when imported')
