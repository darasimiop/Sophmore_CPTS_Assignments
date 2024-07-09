#include "queue.h"
/*       Test ID: Dequeue Check - DC
          Unit: queue::dequeue() 
          Description: test to determine if queue::dequeue() removes from queue.
Test steps: 
1.    Construct an empty queue object 
2.    Insert elements till queue is full
3.    Invoke queue::dequeue () 
4.    Conditionally evaluate the valued returned by 
queue::Dequeue () 
          Test data: size = 5
          Precondition: queue object is empty 
          Postcondition: queue object has < 5 items in queue
Expected result: queue has < 5 items; True 
          Actual result: --
          Status: working
*/ 
void testDequeue();

/*       Test ID: Enqueue Check - EC
          Unit: queue::Enqueue() 
          Description: test to determine if queue::Enqueue() adds to queue.
Test steps: 
1.    Construct an empty queue object 
2.    Insert elements till queue is 1 away from full
3.    Invoke queue::Enqueue () 
4.    Conditionally evaluate the valued returned by 
queue::Enqueue () 
          Test data: size = 5
          Precondition: queue object is empty 
          Postcondition: queue object has 5 items in queue
Expected result: queue has  5 items; True 
          Actual result: --
          Status: ---
*/ 
void testEnqueue();

/*       Test ID: Peek Check - PC
          Unit: queue::peek() 
          Description: test to determine if queue::peek() adds to queue.
Test steps: 
1.    Construct an empty queue object 
2.    Insert elements till queue is 1 away from full
3.    Invoke queue::peek () 
4.    Conditionally evaluate the valued returned by 
queue::peek () 
          Test data: size = 2
          Precondition: queue object is empty 
          Postcondition: queue object has 2 items in queue
Expected result: queue has 1 as first item; True 
          Actual result: --
          Status: ---
*/ 
void testPeek();

/*       Test ID: Size Check - SC
          Unit: queue::size() 
          Description: test to determine if queue::size() adds to queue.
Test steps: 
1.    Construct an empty queue object 
2.    Insert elements till queue is full
3.    Invoke queue::size () 
4.    Conditionally evaluate the valued returned by 
queue::size () 
          Test data: size = 5
          Precondition: queue object is empty 
          Postcondition: queue object has 5 items in queue
Expected result: queue has 5 items; True 
          Actual result: --
          Status: ---
*/ 
 void testSize();

 /*       Test ID: Empty Queue Check - EQC
          Unit: queue::isEmpty() 
          Description: test to determine if queue::idEmpty returns True if empty and False if not.
Test steps: 
1.    Construct an empty queue object 
2.    Invoke queue::isEmpty () 
3.    Conditionally evaluate the valued returned by 
queue::isEmpty () 
          Test data: size = 0
          Precondition: queue object is empty 
          Postcondition: queue object is empty
Expected result: queue is Empty; True 
          Actual result: --
          Status: working
*/ 
void testISEmpty();
/*       Test ID: Full Queue Check - FQC
          Unit: queue::isFull() 
          Description: test to determine if queue::isFull returns True if full and False if not.
Test steps: 
1.    Construct an empty queue object 
2.    Insert elements till queue is full
2.    Invoke queue::isFull () 
3.    Conditionally evaluate the valued returned by 
queue::isEmpty () 
          Test data: size = 5
          Precondition: queue object is empty 
          Postcondition: queue object is Full
Expected result: queue is Full; True 
          Actual result: --
          Status: working
*/ 
void testIsFull();







