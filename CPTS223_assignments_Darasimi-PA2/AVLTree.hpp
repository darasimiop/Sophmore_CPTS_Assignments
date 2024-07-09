#include "AVLNode.hpp" // Include your AVLNode header here
#include <iostream>
#include <algorithm> // Add this line for std::max


template <typename T>
class AVLTree {
public:
    AVLTree() : root(nullptr) {}

    // Function to return the height of the tree
    int height() const {
        return height(root);
    }

    // Function to insert a value into the tree while maintaining AVL properties
    void insert(T data) {
    root = root-> insert(root, data);

}

    // Function to check if a value exists in the tree
    bool contains(T data) const {
        return contains(root, data);
    }

    // Public method to check if the tree is balanced
    bool isBalanced() const {
        return root->validate();
    }


private:
    AVLNode<T>* root;

    // Private helper function to get the height of a node
    int height(AVLNode<T>* node) const {
        if (node == nullptr) {
            return 0;
        }
        return node->getHeight();
    }

    // Private helper function to check if a value exists in the tree
    bool contains(AVLNode<T>* node, T data) const {
        if (node == nullptr) {
            return false;
        }
        if (data == node->data) {
            return true;
        } else if (data < node->data) {
            return contains(node->left, data);
        } else {
            return contains(node->right, data);
        }
    }


    // Private helper function for right rotation
    AVLNode<T>* rightRotate(AVLNode<T>* y) {
        AVLNode<T>* x = y->left;
        AVLNode<T>* T2 = x->right;

        // Perform the rotation
        x->right = y;
        y->left = T2;

        // Update heights
        y->setHeight(1 + std::max(height(y->left), height(y->right)));
        x->setHeight(1 + std::max(height(x->left), height(x->right)));

        return x;
    }

    // Private helper function for left rotation
    AVLNode<T>* leftRotate(AVLNode<T>* x) {
        AVLNode<T>* y = x->right;
        AVLNode<T>* T2 = y->left;

        // Perform the rotation
        y->left = x;
        x->right = T2;

        // Update heights
        x->setHeight(1 + std::max(height(x->left), height(x->right)));
        y->setHeight(1 + std::max(height(y->left), height(y->right)));

        return y;
    }
};
