#include <iostream>
#include <algorithm> // Add this line for std::max


template <typename T>
class AVLNode {
public:
    // Public data members 
    T data; 
    AVLNode* left;
    AVLNode* right; 
    int height_; 

    // Constructor to initialize an AVLNode with data 
    AVLNode(T value) : data(value), left(nullptr), right(nullptr), height_(1) {}

    // Public member functions (you can add more as needed)
    int getHeight() const {
        return height_; 
    }

    void setHeight(int newHeight) {
        height_ = newHeight; 
    }
    // Other public functions

// Function to validate if the tree is balanced
    bool validate() const {
        if (this == nullptr) {
            return true;
        }
        int balance = getBalance(this);
        if (balance < -1 || balance > 1) {
            return false;
        }
        return left->validate() && right->validate();
    }

// Function to insert a value into the AVL tree
    AVLNode<T>* insert(AVLNode<T>* node, T data) {
        if (node == nullptr) {
            return new AVLNode<T>(data);
        }

        // Perform standard BST insertion
        if (data < node->data) {
            node->left = insert(node->left, data);
        } else if (data > node->data) {
            node->right = insert(node->right, data);
        } else {
            // Duplicate data not allowed
            return node;
        }

        // Update height of this ancestor node
        node->setHeight(1 + std::max(height(node->left), height(node->right)));

        // Get the balance factor
        int balance = getBalance(node);

        // Perform rotations if needed
        if (balance > 1) {
            if (data < node->left->data) {
                return rightRotate(node);
            } else {
                node->left = leftRotate(node->left); // Perform left rotation first
                return rightRotate(node);
            }
        }
        if (balance < -1) {
            if (data > node->right->data) {
                return leftRotate(node);
            } else {
                node->right = rightRotate(node->right); // Perform right rotation first
                return leftRotate(node);
            }
        }

        return node;
    }

// Function to remove a value from the AVL tree
AVLNode<T>* remove(AVLNode<T>* node, T data) {
    if (node == nullptr) {
        return node;
    }

    if (data < node->data) {
        node->left = remove(node->left, data);
    } else if (data > node->data) {
        node->right = remove(node->right, data);
    } else {
        // Node with the value to be removed found

        // If one child or no child
        if (node->left == nullptr || node->right == nullptr) {
            AVLNode<T>* temp = node->left ? node->left : node->right;

            if (temp == nullptr) {
                // No child
                temp = node;
                node = nullptr;
            } else {
                // One child
                *node = *temp; // Copy the contents of the non-empty child
            }

            delete temp;
        } else {
            // Node with two children: Get the inorder successor (smallest in the right subtree)
            AVLNode<T>* temp = findMin(node->right);

            // Copy the inorder successor's data to this node
            node->data = temp->data;

            // Delete the inorder successor
            node->right = remove(node->right, temp->data);
        }
    }

    if (node == nullptr) {
        return node;
    }

    // Update height of this ancestor node
    node->setHeight(1 + std::max(height(node->left), height(node->right)));

    // Get the balance factor
    int balance = getBalance(node);

    // Perform rotations if needed
    if (balance > 1) {
        if (getBalance(node->left) >= 0) {
            return rightRotate(node);
        } else {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
    }
    if (balance < -1) {
        if (getBalance(node->right) <= 0) {
            return leftRotate(node);
        } else {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
    }
    return node;

}


private:
    // Private data members
    AVLNode<T>* root;

    // Private member functions

    // Function to calculate the height of a node
    int height(const AVLNode<T>* node) const {
    if (node == nullptr) {
        return 0;
    }
    return node->getHeight();
}


    // Function to get the balance factor of a node
    int getBalance(const AVLNode<T>* node) const {
    if (node == nullptr) {
        return 0;
    }
    return height(node->left) - height(node->right);
}


    // Function to perform a right rotation
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

    // Function to perform a left rotation
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

    

    // Implement other helper functions and rotations as needed
};
