#include "queue.h"
#include <limits>
// Constructor to initialize queue
queue::queue(int size)
{
    arr = new int[size];
    capacity = size;
    front = 0;
    rear = -1;
    count = 0;
};

// Destructor to free memory allocated to the queue
queue::~queue()
{
    delete arr; // you are not required to test this function;
    // however, are there issues with it?
};

// Utility function to remove front element from the queue
void queue::dequeue()
{
    // check for queue underflow
    if (isEmpty())
    {
        cout << "UnderFlow\nProgram Terminated\n";
        return;
    }

    cout << "Removing " << arr[front] << '\n';

    front = (front + 1) % capacity;
    count--;
};

// Utility function to add an item to the queue
void queue::enqueue(int item)
{
    // check for queue overflow
    if (isFull())
    {
        cout << "OverFlow\nProgram Terminated\n";
        return;
    }

    cout << "Inserting " << item << '\n';

    rear = (rear + 1) % capacity;
    arr[rear] = size();
    count++;
};

// Utility function to return front element in the queue
int queue::peek()
{
    if (isEmpty())
    {
        cout << "UnderFlow\nProgram Terminated\n";
        return numeric_limits<int>::min();
    }
    return arr[rear];
};

// Utility function to return the size of the queue
int queue::size()
{
    return count;
};

// Utility function to check if the queue is empty or not
bool queue::isEmpty()
{
    return (size() == 0);
};

// Utility function to check if the queue is full or not
bool queue::isFull()
{
    return (size()-1 == capacity);
};

