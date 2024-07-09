# Import necessary modules and classes from Hw5.py
from Hw5 import Buffer, Literal, Array, Name, Block, Operators, read_expr, read_block_expr

# Define test cases
def test_buffer_pop_first():
    # Test Buffer pop_first method
    data = "hello"
    buffer = Buffer(data)
    assert buffer.pop_first() == "h"
    assert buffer.pop_first() == "e"
    print("buffer test passed successfully!")


def test_literal_evaluate():
    # Test Literal evaluate method
    literal = Literal(42)
    ops = Operators("static")  # or "dynamic", depending on your requirements
    literal.evaluate(ops)
    assert ops.opstack == [42]
    print("literal tests passed successfully!")


# Add more test cases as needed...

# Run test cases
if __name__ == "__main__":
    test_buffer_pop_first()
    test_literal_evaluate()
    
    # Add calls to other test functions here...
    
