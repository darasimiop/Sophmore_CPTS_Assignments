#include "testQueue.h"
/*
1)Lack of Return Value in testPeek() Function:


In the testPeek() function, I declare a return type of int but
 do not include a return statement. This can lead to unexpected behavior
  and compiler warnings. The function should return an integer value.

2)Undefined Behavior in testDequeue() and testEnqueue() Functions:

In both testDequeue() and testEnqueue() functions, I iterate using a loop that 
goes beyond the allocated size of the queue. This can lead to undefined behavior
 as I'm  accessing memory out of bounds.

 3)Undefined Behavior in testISEmpty() Function:

In the testISEmpty() function, I do not return a value
 from the function declared as bool. This can lead to undefined behavior.
  The function should return a bool value.

  4) Lack of Return Statement in testSize() Function:

  In the testSize() function, I declare a return type of int but do not 
  include a return statement. This can lead to unexpected behavior and compiler 
  warnings. The function should return an integer value.

5)Inconsistent Test Function Naming Conventions:

The naming conventions for your test functions are inconsistent.
 Some functions are named with "Passed" or "Failed" in the description, 
 while others do not follow this pattern. For consistency, I should either 
 include or exclude "Passed" and "Failed" consistently in all test function names.

These are the five poor attributes identified in my code. I made the 
necessary corrections to address these issues.

*/

int main(){


    testIsFull();
    testDequeue();
    testEnqueue();
    testPeek();
    testSize();
    testISEmpty();
    return 0;
}

