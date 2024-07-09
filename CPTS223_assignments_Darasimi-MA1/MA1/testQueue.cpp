#include "testQueue.h"

void testDequeue(){
    int temp_size = 5;
    queue testQueue(temp_size); //empty object with maximum size of 5

    // populating queue till it's full
    for(int i = 0; i < 5; i++){
        testQueue.enqueue(i);
    }

    //deleting one element 
    for(int i = 0; i < 1; i++){
        testQueue.dequeue();
    }

    // evaluating the value returned by .dequeue()
    if (testQueue.size() == 4){
        cout<< "Test Case  Dequeue Passed!"<<endl;
    }else{
        cout<< "Test Case Dequeue Failed!"<<endl;    
    }

}

void testEnqueue(){
     int temp_size = 6;
    queue testQueue(temp_size); //empty object with maximum size of 6

     // populating queue till it's one away
    for(int i = 0; i < 4; i++){
        testQueue.enqueue(i);
    }

    //adding one element 
    for(int i = 0; i < 1; i++){
        testQueue.enqueue(i);
    }

    // evaluating the value returned by .enqueue()
    if (testQueue.size() == 5){
        cout<< "Test Case Enqueue Passed!"<<endl;
    }else{
        cout<< "Test Case Enqueue Failed!"<<endl;    
    }

}

void testPeek(){
    queue test; 
    test.enqueue(1);
    test.enqueue(3);
    if (test.peek() == 1){
        cout<< "Test Case Peek Passed!"<<endl;
    }else{
        cout<< "Test Case Peek Failed!"<<endl;
    }

}

 void testSize(){
     int temp_size = 6;
    queue testQueue(temp_size); //empty object with maximum size of 5

    // populating queue till it's full
    for(int i = 0; i <= 5; i++){
        testQueue.enqueue(i);
    }

    // evaluating the value returned by .isFull()
    if (testQueue.size() == 6){
        cout<< "Test Case Size Passed!"<<endl;
    }else{
        cout<< "Test Case is Size Failed!"<<endl;    
    }
 }

void testISEmpty(){
    int temp_size = 5;
    queue testQueue(temp_size); //empty object with maximum size of 5

    // evaluating the value returned by .isEmpty()
    if (testQueue.isEmpty()){
        cout<< "Test Case isEmpty Passed!"<<endl;
    }else{
        cout<< "Test Case isEmpty Failed!"<<endl;    
    }
}


void testIsFull(){

    int temp_size = 5;
    queue testQueue(temp_size); //empty object with maximum size of 5

    // populating queue till it's full
    for(int i = 0; i <= 5; i++){
        testQueue.enqueue(i);
    }

    // evaluating the value returned by .isFull()
    if (testQueue.isFull()){
        cout<< "Test Case isFULL Passed!"<<endl;
    }else{
        cout<< "Test Case is FULL Failed!"<<endl;    
    }

}