# Hw5.py

# ---------------------------------------------------
#   Buffer Module
# ---------------------------------------------------

class Buffer:
    """
    A Buffer provides a way of dealing with a sequence of tokens.
    """

    def __init__(self, data):
        """Create a new buffer taking data as its contents."""
        self.data = data
        self.offset = 0

    def pop_first(self):
        """Pop and return the first element in the buffer."""
        if self.offset < len(self.data):
            char = self.data[self.offset]
            self.offset += 1
            return char
        return None

    def current(self):
        """Return the current character in the buffer."""
        if self.offset < len(self.data):
            return self.data[self.offset]
        return None


# ---------------------------------------------------
#   psItems Module
# ---------------------------------------------------

class Literal:
    """
    Represents a literal value in PostScript.
    """

    def __init__(self, value):
        self.value = value

    def evaluate(self, ops):
        ops.opPush(self.value)


class Array:
    """
    Represents an array in PostScript.
    """

    def __init__(self, value):
        self.value = value

    def evaluate(self, ops):
        for item in self.value:
            if isinstance(item, Literal):
                ops.opPush(item.value)
            elif isinstance(item, (int, float, bool)):
                ops.opPush(item)
            else:
                raise TypeError(f"Invalid item in array: {item}")





class Name:
    """
    Represents a name (variable or function) in PostScript.
    """

    def __init__(self, var_name):
        self.var_name = var_name

    def evaluate(self, ops):
        value = ops.lookup(self.var_name)
        ops.opPush(value)


class Block:
    """
    Represents a block (code array) in PostScript.
    """

    def __init__(self, value):
        self.value = value

    def evaluate(self, ops):
        for expr in self.value:
            expr.evaluate(ops)


# ---------------------------------------------------
#   psOperators Module
# ---------------------------------------------------

class Operators:
    def __init__(self, scoperule):
        self.opstack = []
        self.dictstack = []
        self.scoperule = scoperule

        self.builtin_operators = {
            "def": self.psDef,
            "if": self.psIf,
            "ifelse": self.psIfelse,
            "repeat": self.repeat,
            "roll": self.roll,
            "for": self.psFor,
            "forall": self.forall,
            "exch": self.exch,
            "clear": self.clear,
            "copy": self.copy,
            "dup": self.dup,
            "stack": self.stack,
            "pop": self.pop,
            "astore": self.astore,
            "aload": self.aload,
            "putinterval": self.putinterval,
            "getinterval": self.getinterval,
            "length": self.length,
            "array": self.array,
            "gt": self.gt,
            "lt": self.lt,
            "eq": self.eq,
            "mod": self.mod,
            "mul": self.mul,
            "define": self.define,
            "lookup": self.lookup,
            "dictPush": self.dictPush,
            "dictPop": self.dictPop,
            "opPush": self.opPush,
            "opPop": self.opPop,
            "add": self.add,
            "count": self.count,
            "sub": self.sub,
        }

    # Other methods from psOperators.py go here...

# ---------------------------------------------------
#   psParser Module
# ---------------------------------------------------

import string
from buffer import Buffer
from psItems import Literal, Array, Name, Block

# Constants
SYMBOL_STARTS = set(string.ascii_lowercase + string.ascii_uppercase + "_" + "/")
SYMBOL_INNERS = SYMBOL_STARTS | set(string.digits)
NUMERAL = set(string.digits + "-.")
WHITESPACE = set(" \t\n\r")
DELIMITERS = set("(){}[]")
BOOLEANS = set(["true", "false"])

# ---------------------------------------------------
#   psParser Module
# ---------------------------------------------------

import string
from buffer import Buffer
from psItems import Literal, Array, Name, Block

# Constants
SYMBOL_STARTS = set(string.ascii_lowercase + string.ascii_uppercase + "_" + "/")
SYMBOL_INNERS = SYMBOL_STARTS | set(string.digits)
NUMERAL = set(string.digits + "-.")
WHITESPACE = set(" \t\n\r")
DELIMITERS = set("(){}[]")
BOOLEANS = set(["true", "false"])

# Tokenization functions

def tokenize(s):
    """
    Splits the string s into tokens and returns a list of them.
    """
    src = Buffer(s)
    tokens = []
    while True:
        token = next_token(src)
        if token is None:
            return tokens
        tokens.append(token)

def take(src, allowed_characters):
    """
    Returns a string of filtered allowed characters.
    """
    result = ""
    while src.current() in allowed_characters:
        result += src.pop_first()
    return result

def next_token(src):
    """
    Returns the next token from the given Buffer object.
    """
    take(src, WHITESPACE)  # skip whitespace
    c = src.current()
    if c is None:
        return None
    elif c in NUMERAL:
        literal = take(src, NUMERAL)
        try:
            return int(literal)
        except ValueError:
            try:
                return float(literal)
            except ValueError:
                raise SyntaxError("'{}' is not a numeral".format(literal))
    elif c in SYMBOL_STARTS:
        sym = take(src, SYMBOL_INNERS)
        if sym in BOOLEANS:
            return bool(sym)
        else:
            return sym
    elif c in DELIMITERS:
        src.pop_first()
        return c
    else:
        raise SyntaxError("'{}' is not a token".format(c))

# Parser functions

def read_expr(src):
    """
    Converts the next token in the given Buffer to an expression.
    """
    ARRAY_INITIATOR = "["
    ARRAY_DELIMETER = "]"
    CODE_ARRAY_INITIATOR = "{"
    CODE_ARRAY_DELIMETER = "}"

    token = src.pop_first()
    if token is None:
        raise SyntaxError("Incomplete expression")
    elif is_literal(token):
        literal_token = Literal(value=token)
        return literal_token
    elif is_name(token):
        name_token = Name(var_name=token)
        return name_token
    elif token == ARRAY_INITIATOR:
        array_token = read_block_expr(src=src, delimiter=ARRAY_DELIMETER)
        new_array_token = Array(value=array_token)
        return new_array_token
    elif token == CODE_ARRAY_INITIATOR:
        code_array_token = read_block_expr(src=src, delimiter=CODE_ARRAY_DELIMETER)
        new_code_array_token = Block(value=code_array_token)
        return new_code_array_token
    else:
        raise SyntaxError(f"'{token}' is not the start of an expression")

def read_block_expr(src, delimiter):
    """
    Returns the constant array or code array enclosed within matching [] or  {} parentheses.
    """
    s = []
    while src.current() != delimiter:
        if src.current() is None:
            raise SyntaxError("Doesn't have a matching '{}'!".format(delimiter))
        s.append(read_expr(src))
    src.pop_first()  # Pop the delimiter
    return s

def is_literal(s):
    """
    Checks if the given token is a literal - primitive constant value.
    """
    return isinstance(s, int) or isinstance(s, float) or isinstance(s, bool)

def is_name(s):
    """Checks if the given token is a variable or function name."""
    return isinstance(s, str) and s not in DELIMITERS


# ---------------------------------------------------
#   repl Module
# ---------------------------------------------------

try:
    import readline
except ImportError:
    pass
import sys

from psParser import read
from psOperators import Operators

# REPL code...

if __name__ == '__main__':
    static = len(sys.argv) >= 2 and ('--static' in sys.argv)
    read_only = len(sys.argv) >= 2 and ('--read' in sys.argv)

    # Create the PostScript stack
    if static:
        psstacks = Operators("static")
    else:
        psstacks = Operators("dynamic")

    while True:
        try:
            user_input = input('<ssps> ')
            expr_list = read(user_input)
            for expr in expr_list:
                if read_only:
                    print(repr(expr))
                else:
                    expr.evaluate(psstacks)
                psstacks.cleanTop()
        except (SyntaxError, NameError, TypeError, Exception) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print()
            break
# ---------------------------------------------------
#   utils Module
# ---------------------------------------------------

def comma_separated(xs):
    """Convert each value in the sequence xs to a string, and separate them
    with commas.
    """
    return ', '.join([str(x) for x in xs])


# ---------------------------------------------------
#   Main Program
# ---------------------------------------------------

if __name__ == '__main__':
    # Imports
    from psParser import read
    from psOperators import Operators

    # Class Definition: Define your Hw5 class, which will likely include methods for running the PostScript interpreter,
    # handling user input, and managing the interpreter's state.

    # Main Execution: Write the code that runs the read-eval-print loop (REPL) or any other logic for executing PostScript
    # code and interacting with the interpreter.

    # Initialize the operator stack (choose either "static" or "dynamic" scoping)
    static = False  # or True if you want static scoping
    psstacks = Operators("static" if static else "dynamic")

    # REPL code: Run a read-eval-print loop
    while True:
        try:
            user_input = input('<ssps> ')
            expr_list = read(user_input)
            for expr in expr_list:
                expr.evaluate(psstacks)
            # You may want to print the state of the operator stack after each expression evaluation
            print("Opstack:", psstacks.opstack)
            print("Dictstack:", psstacks.dictstack)
        except (SyntaxError, NameError, TypeError, Exception) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print()  # Blank line for clarity
            break  # Exit while loop (and end program)
