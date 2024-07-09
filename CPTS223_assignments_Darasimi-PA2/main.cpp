#include "AVLTree.hpp"
#include <vector>
#include <cstdlib>
#include <ctime>

int main()
{
std::vector<int> ascendingData;
    std::vector<int> descendingData;
    std::vector<int> randomData;

    // Ascending order data
    for (int i = 1; i <= 100; ++i) {
        ascendingData.push_back(i);
    }

    // Descending order data
    for (int i = 100; i >= 1; --i) {
        descendingData.push_back(i);
    }

    // Random order data
    srand(static_cast<unsigned>(time(nullptr)));
    for (int i = 1; i <= 100; ++i) {
        randomData.push_back(rand() % 100 + 1);
    }
    

    AVLTree<int> ascendingTree;
    AVLTree<int> descendingTree;
    AVLTree<int> randomTree;

    for (int data : ascendingData) {
        ascendingTree.insert(data);
    }

    for (int data : descendingData) {
        descendingTree.insert(data);
    }

    for (int data : randomData) {
        randomTree.insert(data);
    }

// Print the height of each tree
    std::cout << "Ascending Tree Height: " << ascendingTree.height() << std::endl;
    std::cout << "Descending Tree Height: " << descendingTree.height() << std::endl;
    std::cout << "Random Tree Height: " << randomTree.height() << std::endl;

    // Check if each tree is balanced
    if (ascendingTree.isBalanced()) {
        std::cout << "Ascending Tree is balanced." << std::endl;
    } else {
        std::cout << "Ascending Tree is not balanced." << std::endl;
    }

    if (descendingTree.isBalanced()) {
        std::cout << "Descending Tree is balanced." << std::endl;
    } else {
        std::cout << "Descending Tree is not balanced." << std::endl;
    }

    if (randomTree.isBalanced()) {
        std::cout << "Random Tree is balanced." << std::endl;
    } else {
        std::cout << "Random Tree is not balanced." << std::endl;
    }


 // Loop over numbers and check if they exist in each tree
    for (int i = 1; i <= 100; ++i) {
        if (ascendingTree.contains(i)) {
            std::cout << "Ascending Tree contains " << i << std::endl;
        } else {
            std::cout << "Ascending Tree does not contain " << i << std::endl;
        }

        if (descendingTree.contains(i)) {
            std::cout << "Descending Tree contains " << i << std::endl;
        } else {
            std::cout << "Descending Tree does not contain " << i << std::endl;
        }

        if (randomTree.contains(i)) {
            std::cout << "Random Tree contains " << i << std::endl;
        } else {
            std::cout << "Random Tree does not contain " << i << std::endl;
        }
    }

return 0;
}