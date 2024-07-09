#include "data.hpp"
#pragma once 
template <class NODETYPE>
class Node{
public:
    // default constructor with no arguments 
    Node(){
        this->data = NULL;
        this->pNext = nullptr;
    }

    // constructor with arguments
    Node(Data newData, Node<NODETYPE>* nextp = nullptr){
        this->data = newData;
        this->pNext = nextp;
    }

    ~Node() {};

    Data getData(){
        return this->data;
    }

    Node<NODETYPE>* getNextptr(void) const{
        return this->pNext;
    }

    void setData(Data* newData){
        data.setCommand(newData->getCommand());
        data.setDescription(newData->getDescription());
        data.setPoints(newData->getPoints());
    }

    void setNextptr(Node<NODETYPE>* newNode){
        pNext = newNode;
    }

private:
    Data data;
    Node<NODETYPE>* pNext;
};

