#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  # assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.
def opPop():
    if opstack:
        return opstack.pop()
    else:
        print("Error: Operand stack is empty.")

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  # assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name
def dictPop():
    if dictstack:
        return dictstack.pop()
    else:
        print("Error: Dictionary stack is empty.")

def dictPush(d):
    dictstack.append(d)

def define(name, value):
    if dictstack:
        dictstack[-1][name] = value
    else:
        dictstack.append({})
        dictstack[-1][name] = value
        print("Error: No dictionary in the dictionary stack.")

def lookup(name):
    for dictionary in reversed(dictstack):
        if '/' + name in dictionary:
            return dictionary['/' + name]
    return None

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            opPush(op1 + op2)
        elif isinstance(op1, str) and isinstance(op2, str):
            opPush(op1 + op2)
        else:
            opPush(op1)
            opPush(op2)
            print("Error: Invalid operand types for addition.")
    else:
        print("Error: Not enough operands on the stack for addition.")

def sub():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            opPush(op1 - op2)
        else:
            print("Error: Invalid operand types for subtraction.")
    else:
        print("Error: Not enough operands on the stack for subtraction.")

def mul():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            opPush(op1 * op2)
        else:
            print("Error: Invalid operand types for multiplication.")
    else:
        print("Error: Not enough operands on the stack for multiplication.")

def div():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            if op2 != 0:
                opPush(op1 / op2)
            else:
                print("Error: Division by zero.")
        else:
            print("Error: Invalid operand types for division.")
    else:
        print("Error: Not enough operands on the stack for division.")

def mod():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 != 0:
                opPush(op1 % op2)
            else:
                print("Error: Modulo by zero.")
        else:
            print("Error: Invalid operand types for modulo.")
    else:
        print("Error: Not enough operands on the stack for modulo.")

def eq():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        opPush(op1 == op2)
    else:
        print("Error: Not enough operands on the stack for equality comparison.")

def lt():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        opPush(op1 < op2)
    else:
        print("Error: Not enough operands on the stack for less than comparison.")

def gt():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        opPush(op1 > op2)
    else:
        print("Error: Not enough operands on the stack for greater than comparison.")

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    if len(opstack) >= 1:
        opPush(len(opPop()) - 2)  # Exclude parentheses
    else:
        print("Error: Operand stack is empty.")

def get():
    if len(opstack) >= 2:
        index = opPop()
        string = opPop()
        if isinstance(string, str) and isinstance(index, int) and 0 <= index < len(string):
            opPush(ord(string[index + 1]))
        else:
            print("Error: Invalid parameters for get operator.")
    else:
        print("Error: Operand stack is empty.")

def getinterval():
    if len(opstack) >= 3:
        count = opPop()
        index = opPop()
        string = opPop()
        if isinstance(string, str) and isinstance(index, int) and isinstance(count, int) and index >= 0 and count >= 0:
            opPush("(" + string[index + 1:index + 1 + count] + ")")
        else:
            print("Error: Invalid parameters for getinterval operator.")
    else:
        print("Error: Not enough operands on the stack for getinterval operator.")

def put():
    if len(opstack) >= 3:
        value = opPop()
        index = opPop()
        string = opPop()
        if isinstance(string, str) and isinstance(index, int) and isinstance(value, int) and 0 <= index < len(string):
            string = removeparenthesis(string)
            opPush('('+ string[:index] + chr(value) + string[index + 1:] + ')')
        else:
            print("Error: Invalid parameters for put operator.")
    else:
        print("Error: Not enough operands on the stack for put operator.")

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, exch, pop, copy, clear, stack
def dup():
    if opstack:
        opPush(opstack[-1])
    else:
        print("Error: Operand stack is empty.")

def exch():
    if len(opstack) >= 2:
        op2 = opPop()
        op1 = opPop()
        opPush(op2)
        opPush(op1)
    else:
        print("Error: Not enough operands on the stack for exchange operator.")

def pop():
    if opstack:
        opPop()
    else:
        print("Error: Operand stack is empty.")

def copy():
    if len(opstack) >= 1:
        count = opPop()
        if isinstance(count, int) and count >= 0:
            opstack.extend(opstack[-count:])
        else:
            print("Error: Invalid parameter for copy operator.")
    else:
        print("Error: Operand stack is empty.")

def clear():
    del opstack[:]

def stack():
    #print("== Operand Stack ==")
    for value in opstack[::-1]:
        print(value)
    #print("===================")

def roll():
    if len(opstack) >= 3:
        k = opPop()
        j = opPop()
        n = []
        if isinstance(j, int) and isinstance(k, int):
            for i in range(0, j):
                n.append(opPop())
                n.reverse()

            for times in range(0, k):
                temp = n [ len(n) - 1]
                n = n[: len(n) - 1 ]                
                n = [temp] + n

            for val in n:
                opPush(val)
        else:
            print("Error: Invalid parameters for roll operator.")
    else:
        print("Error: Not enough operands on the stack for roll operator.")

            # if n > 0:
            #     opstack[-n:] = opstack[-n - j:] + opstack[-n:-n - j]
            #     if k < 0:
            #         k = -k
            #         j = -j
            # elif n < 0:
            #     opstack[-n:] = opstack[-n - j:] + opstack[-n:-n - j]
            #     if k > 0:
            #         k = -k
            #         j = -j
            # opstack[-n - j:] = opstack[-n - j - k:] + opstack[-n - j:-n - j - k]
       # else:
          #  print("Error: Invalid parameters for roll operator.")
    #else:
      #  print("Error: Not enough operands on the stack for roll operator.")


#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
def psDict():
    opPush({})

def begin():
    dictPush({})

def end():
    if dictstack:
        dictPop()
    else:
        print("Error: Dictionary stack is empty.")

def psDef():
    if len(opstack) >= 2:
        value = opPop()
        name = opPop()
        define(name, value)
    else:
        print("Error: Not enough operands on the stack for psDef operator.")

#---------------------------- 5% -------------------------------------
# Testing functions
def testAdd():
    opPush(2)
    opPush(3)
    add()
    if opPop() == 5:
        print("add function works correctly")
    else:
        print("add function did not work correctly")

def testSub():
    opPush(7)
    opPush(3)
    sub()
    if opPop() == 4:
        print("sub function works correctly")
    else:
        print("sub function did not work correctly")

def testMul():
    opPush(5)
    opPush(3)
    mul()
    if opPop() == 15:
        print("mul function works correctly")
    else:
        print("mul function did not work correctly")

def testDiv():
    opPush(21)
    opPush(7)
    div()
    if opPop() == 3:
        print("div function works correctly")
    else:
        print("div function did not work correctly")

def testMod():
    opPush(21)
    opPush(7)
    mod()
    if opPop() == 0:
        print("mod function works correctly")
    else:
        print("mod function did not work correctly")

# Testing all functions
def testAll():
    testAdd()
    testSub()
    testMul()
    testDiv()
    testMod()

if __name__ == "__main__":
    testAll()

def removeparenthesis(s):
    """
    Removes parentheses from a given string.

    Parameters:
        s (str): The string from which parentheses will be removed.

    Returns:
        str: The string with parentheses removed.
    """
    return s.replace("(", "").replace(")", "")


    