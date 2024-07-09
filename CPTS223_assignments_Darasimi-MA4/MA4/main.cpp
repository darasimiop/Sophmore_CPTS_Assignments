#include "OpenMP.hpp"
#include "Heap.hpp"

void runOpenMP() {
    hello_world();
    cal_sum();
    cal_max();
}

void runHeap() {
    printf("\nStart runHeap()\n");
    int data_size = 10000;
    int* data = new int[data_size];
    for (int i = 0; i < data_size; ++i) {
        data[i] = rand() % data_size;
    }
    auto *hp = new Heap<int>();
    for (int i = 0; i < data_size; ++i) {
        hp->push(data[i]);
    }

    // Sort these values using stl
    std::vector<int> vect(data, data + data_size);
    std::sort(vect.begin(), vect.end());

    // Update the loop to check if the heap is not empty before popping
    int i = 0;
    while (!hp->empty()) {
        assert(vect[i] == hp->pop());
        ++i;
    }

    printf("\nStart runHeap(): assert pass!\n");
}

int main(int argc, char* argv[])
{
    runOpenMP();
    runHeap();
}