"""Parts of the lexer and parser code was adopted from https://composingprograms.com/. 
The code has been changed according to Postscript syntax. 
https://creativecommons.org/licenses/by-sa/3.0/
"""
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
#   Lexer #
# ---------------------------------------------------


def tokenize(s):
    """
    Splits the string s into tokens and returns a list of them.
    >>> tokenize('/addsq { /sq {dup mul} def sq exch sq add exch sq add } def  2 3 4 addsq')
    """
    src = Buffer(s)
    tokens = []
    while True:
        token = next_token(src)
        if token is None:
            # print(tokens)
            return tokens
        tokens.append(token)


""" Takes allowed characters only. Filters out everything else.  """


def take(src, allowed_characters):
    """
    returns a string of filtered allowed characters.
    """
    result = ""
    while src.current() in allowed_characters:
        result += src.pop_first()
    return result


"""Returns the next token from the given Buffer object. """


def next_token(src):
    """
    parses the src argument and returns either a Numeral[int or float], Symbols[words or bools] or Delimiters
    """
    take(src, WHITESPACE)  # skip whitespace
    c = src.current()  # returns the current element or none
    if c is None:
        return None
    elif c in NUMERAL:
        literal = take(src, NUMERAL)  # returns a string of allowed numerals
        try:
            return int(literal)  # converts it to an Integer
        except ValueError:
            try:
                return float(literal)  # converts it to a float
            except ValueError:
                raise SyntaxError("'{}' is not a numeral".format(literal))
    elif c in SYMBOL_STARTS:
        sym = take(
            src, SYMBOL_INNERS
        )  # returns a string of alphabetic letters in lower and higher case
        if sym in BOOLEANS:
            return bool(sym)
        else:
            return sym
    elif c in DELIMITERS:
        src.pop_first()
        return c
    else:
        raise SyntaxError("'{}' is not a token".format(c))


# ---------------------------------------------------
#   Parser #
# ---------------------------------------------------

# Helper functions for the parser.


def is_literal(s):
    """
    Checks if the given token is a literal - primitive constant value.
    """
    return isinstance(s, int) or isinstance(s, float) or isinstance(s, bool)


def is_object(s):
    """
    Checks if the given token is an array object.
    """
    return isinstance(s, list)


def is_name(s):
    """Checks if the given token is a variable or function name.
    The name can either be:
    - a name constant (where the first character is /) or
    - a variable (or function)
    """
    return isinstance(s, str) and s not in DELIMITERS


def read_block_expr(src, delimiter):
    """
    Returns the constant array or code array enclosed within matching [] or  {} paranthesis. delimiter is either ']' or '}'
    """
    s = []
    while src.current() != delimiter:
        if src.current() is None:
            raise SyntaxError("Doesn't have a matching '{}'!".format(delimiter))
        s.append(read_expr(src))
    "Pop the `]`."
    src.pop_first()
    return s


def read_expr(src: Buffer):
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


def read(s):
    """
    Parse an expression from a string. If the string does not contain an
    expression, None is returned. If the string cannot be parsed, a SyntaxError
    is raised.
    """
    # reading one token at a time
    try:
        src = Buffer(tokenize(s))
        print(src)
        out = []
        while src.current() is not None:
            out.append(read_expr(src))

        # check for detected expressions
        if len(out) == 0:
            return None
        else:
            return out
    except SyntaxError:
        raise SyntaxError(f"{s} can not be parsed.")
