
from psItems import Value, ArrayValue, FunctionValue, Name


class Operators:
    def __init__(self,scoperule):
        # stack variables
        self.opstack = []  # assuming top of the stack is the end of the list
        self.dictstack: list[tuple] = []  #e.g. (1,{<FunctionValue>}) == Activation record, smth like that  
        # assuming top of the stack is the end of the list,
        # a stack of tuples where each tuple contains an int index(static link i.e. the position of the parent scope in the list) and a dict
        self.scoperule = scoperule

        # The builtin operators supported by our interpreter
        self.builtin_operators = {
            # TO-DO in part1
            # include the key value pairs where he keys are the PostScrip opertor names and the values are the function values that implement that operator.
            # Make sure **not to call the functions**
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

    # -------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """

    def opPop(self):
        return self.opstack.pop()

    """
       Helper function. Pushes the given value to the opstack.
    """

    def opPush(self, value):
        self.opstack.append(value)

    # ------- Dict Stack Operators --------------

    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """

    def dictPop(self):
        return self.dictstack.pop()

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """

    def dictPush(self, d):
        if isinstance(d,tuple):
            self.dictstack.append(d)
        else:
            raise ValueError(f'{d} is not an actvaivation record')

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """

    def define(self, name: str | int, value):
        if self.dictstack:
            tup = self.dictPop()
            tup[1][name] = value
            self.dictPush(tup)
        else:
            newDict = {}
            newDict[name] = value
            newtp = (0,newDict)
            self.dictPush(newtp)
    
        


    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    def lookup(self, name):
        name = "/" + name
        if self.scoperule == "dynamic":
            self.dictstack.reverse()
            for link ,dct in self.dictstack:
                if name in dct.keys():
                    self.dictstack.reverse()
                    return dct[name]
            self.dictstack.reverse()
            raise LookupError(f'{name} not found in dictstack')
        else:
            link = len(self.dictstack) -1
            prevlink = -1
            while True:
                if name in self.dictstack[link][1].keys():
                    return self.dictstack[link][1][name]
                else:
                    if link == prevlink: 
                        raise LookupError(f'{name} not found in dictstack')
                prevlink = link
                link = self.dictstack[link-1][0]


    def static_link_helper(self,functVal):
        self.dictstack.reverse()
        index = len(self.dictstack) - 1
        for link, dct in self.dictstack:
            if functVal in dct.values():
                self.dictstack.reverse()
                return index
            index -= 1
        self.dictstack.reverse()
        raise LookupError(f'{functVal} not found in dictstack')

    # ------- Arithmetic Operators --------------

    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """

    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()  # top value
            op2 = self.opPop()  # bottom value
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)  # bottom value
                self.opPush(op1)  # top value
        else:
            print("Error: add expects 2 operands")

    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """

    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 - op1)
            else:
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """

    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """

    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 % op1)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)

    # ---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """

    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if op1 == op2:
                self.opPush(True)
            else:
                self.opPush(False)

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """

    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if op1 > op2:
                self.opPush(True)
            else:
                self.opPush(False)

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """

    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if op1 < op2:
                self.opPush(True)
            else:
                self.opPush(False)

    # ------- Array Operators --------------
    """ 
       Pops the array length (an int value) from the opstack and initializes an array constant (ArrayValue) having the given length. 
       Initializes the elements in the value of the ArrayValue to None. Pushes the ArrayValue to the opstack.
    """

    def array(self):
        potential_length = self.opPop()
        potential_values = []
        if isinstance(potential_length, int):
            objectt = ArrayValue(value=None)
            # allocate space for potential_length of values
            for v in range(potential_length):
                potential_values.append(None)
            objectt.value = potential_values
            self.opPush(objectt)

    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """

    def length(self):
        potential_array = self.opPop()
        if isinstance(potential_array, ArrayValue):
            _len_ = len(potential_array.value)
            self.opPush(_len_)

    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """

    def getinterval(self):
        count = self.opPop()
        start_index = self.opPop()
        end_index = count + start_index
        potential_arr = self.opPop()
        lnt = len(potential_arr.value)
        obj = ArrayValue(None)
        if lnt >= end_index:
            obj.value = potential_arr.value[start_index:end_index]
            self.opPush(obj)
        else:
            raise IndexError("endIndex > arrayLength")

    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """

    def putinterval(self):
        if len(self.opstack) > 2:
            arr1 = self.opPop()
            index = self.opPop()
            arr2 = self.opPop()
            if len(arr2.value) > (len(arr1.value) - index - 1):
                arr2.value[index : index + len(arr1.value)] = arr1.value
            else:
                raise IndexError("index > arrayLength")
        else:
            print("expected 3 operands")

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """

    def aload(self):
        if self.opstack:  # if the list isn't empty
            arr = self.opPop()
            for v in arr.value:
                self.opPush(v)
            self.opPush(arr)

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """

    def astore(self):
        if self.opstack:
            arr = self.opPop()
            obj = ArrayValue(None)
            obj_v = []
            for i in range(len(arr.value)):
                obj_v.append(self.opstack.pop())
            obj_v.reverse()
            obj.value = obj_v
            self.opstack.append(obj)

    # ------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """

    def pop(self):
        self.opPop()

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """
    
    def stack(self):
        op_visual = self.opstack[:]
        dc_visual = self.dictstack[:]
        op_visual.reverse()
        dc_visual.reverse()

        print("===**opstack**===")
        for v in op_visual:
            print(v)
        print("===**dictstack**===")
        i = len(dc_visual) -1 
        for (index,dct) in dc_visual:
            print(f"--- {i} --- {index} ---")
            i -= 1
            for key,value in dct.items():
                print(f"{key} {value}")
        print("=======================")


    """
       Copies the top element in opstack.
    """

    def dup(self):
        if self.opstack:
            orig = self.opPop()
            self.opPush(orig)
            self.opPush(orig)

    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """

    def copy(self):
        self.opstack.reverse()
        count = self.opstack.pop(0)
        if isinstance(count, int):
            v = self.opstack[:count]
            print(v)
            v_ = v[:]
            v_.reverse()
            for i in range(len(v)):
                self.opstack.insert(i, v_.pop())
            self.opstack.reverse()

    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """

    def count(self):
        count = len(self.opstack)
        self.opstack.append(count)

    """
       Clears the opstack.
    """

    def clear(self):
        self.opstack.clear()

    """
       swaps the top two elements in opstack
    """

    def exch(self):
        if self.opstack:
            a, b = self.opPop(), self.opPop()
            self.opPush(a)
            self.opPush(b)

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """

    def roll(self):
        if self.opstack:
            n = self.opPop()
            m = self.opPop()
            sublist = self.opstack[-m:]
            if n > 0:
                for i in range(n):
                    temp = sublist.pop()
                    sublist.insert(0, temp)
            if n < 0:
                n *= -1
                for i in range(n):
                    temp = sublist.pop(0)
                    sublist.append(temp)
            self.opstack[-m:] = sublist


    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """

    def psDef(self):
        if self.opstack:
            value_ = self.opPop()
            name = self.opPop()
            self.define(name=name, value=value_)

    # ------- if/ifelse Operators --------------

    def psIf(self):
        """
        Implements if operator.
        Pops the `ifbody` and the `condition` from opstack.
        If the condition is True, evaluates the `ifbody`.
        """
        ifbody = self.opPop()
        condition = self.opPop()
        if condition:
            if isinstance(ifbody, FunctionValue):
                ifbody.apply(self)
            else:
                ifbody.evaluate(self)

    def psIfelse(self):
        """
        Implements ifelse operator.
        Pops the `elsebody`, `ifbody`, and the condition from opstack.
        If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`.
        """

        elsebody = self.opPop()
        ifbody = self.opPop()
        condition = self.opPop()
        if condition:
            if isinstance(ifbody, FunctionValue):
                ifbody.apply(self)
            else:
                ifbody.evaluate(self)
        else:
            if isinstance(elsebody, FunctionValue):
                elsebody.apply(self)
            else:
                elsebody.evaluate(self)

    # ------- Loop Operators --------------

    def repeat(self):
        """
        Implements repeat operator.
        Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack;
        Evaluates (applies) the `loopbody` `count` times.
        Will be completed in part-2.
        """
        loop_body = self.opPop()
        count = self.opPop()
        if isinstance(loop_body, FunctionValue):
            for i in range(count):
                loop_body.apply(self)
        else:
            for i in range(count):
                loop_body.evaluate(self)

    def psFor(self):
        """
        Implements for operator.
        Pops a CodeArrayValue object, the end index (end), the increment (inc), and the begin index (begin) and
        executes the code array for all loop index values ranging from `begin` to `end`.
        Pushes the current loop index value to opstack before each execution of the CodeArrayValue.
        Will be completed in part-2.
        """
        for_body = self.opPop()
        end_index = self.opPop()
        increment = self.opPop()
        begin_index = self.opPop()
        if isinstance(for_body, FunctionValue):
            for i in range(begin_index, end_index + increment, increment):
                self.opPush(i)
                for_body.apply(self)

    def forall(self):
        """
        Implements forall operator.
        Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack;
        Evaluates (applies) the `codearray` on every value in the `array`.
        Will be completed in part-2.
        """
        codearr = self.opPop()
        arr = self.opPop()
        newarr = []
        for item in arr.value:
            self.opPush(item)
            codearr.apply(self)

    # --- used in the setup of unittests
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []

    def cleanTop(self):
        if len(self.opstack) > 1:
            if self.opstack[-1] is None:
                self.opstack.pop()
