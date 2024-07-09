#include "node.hpp"
#include <fstream>
using std::ofstream;



template <class NODETYPE>
class linked_list {
public:
    linked_list(){
        this->pHead = nullptr;
        this->numCommands = 0; // Initilaze the count 0 
    }

    ~linked_list(){
        this->destroyList();
    }

    void addData(){
        std::fstream sourceFile;
        sourceFile.open("commands.csv");

        char line[100];
        int linelength = 0;
        int i = 0;

        if(!sourceFile)
        {
            cout << "commands.csv not found";
            exit(EXIT_FAILURE);
        }

        while (!sourceFile.eof())
        {
            Data temp("","",0);
            string point, command, description;
            int points = 0;

            sourceFile.getline(line, 100, ',');
            command = line;

            sourceFile.getline(line, 100, ',');
            description = line;

            sourceFile.getline(line, 100, '\n');
            point = line;
            points = stoi(point);


            temp.setCommand(command);
            temp.setDescription(description);
            temp.setPoints(points); 

            insert(temp);

            i++;

        }
        sourceFile.close();
    }

    Node<NODETYPE>* getHeadptr(){
        return this->pHead;
    }

    void setHeadptr(Node<NODETYPE>* newHeadptr){
        this->pHead = newHeadptr;
    }

    void insert(Data newData){

        Node<Data>* newNode = new Node<Data>(newData); //creating a node of type Data. Functionality handled by Node's Constructor
        if(this->pHead == nullptr){
            incrementNumCommands(); 
            this->pHead = newNode;
        } else{

            Node<NODETYPE>* current = pHead;

            // iterate to the last item in the linked list
            while(current->getNextptr() != nullptr){
                current = current->getNextptr();
            }
            incrementNumCommands(); 

            current->setNextptr(newNode);
        }
    }

    int deleteNode(string command){
        int success = 0;

        Node<NODETYPE>* current = this->pHead;
        Node<NODETYPE>* prev = nullptr;

        if(current != nullptr && current->getData().getCommand() == command){
            this->pHead = current->getNextptr();
            delete current;

            success = 1;
            return success;
        }

        while (current != nullptr && current->getData().getCommand() != command)
        {
            prev = current;
            current = current->getNextptr();
            cout << "target not found at the moment ..." << endl;
        }

        if(current == nullptr){
            success = 1;

            return success;
        }

        prev->setNextptr(current->getNextptr());
        delete current;
        success = 1;
        return success;
    }

    void displayList(){
        int i = 0;
        
        Node<NODETYPE>* current = this->pHead;
        cout << "List Items:\n";
        while (current != nullptr)
        {
            i++;
            cout << i << "." << "-" << current->getData().getCommand() 
            << "," << current->getData().getDescription() 
            << "," << current->getData().getPoints() << endl;

            current = current->getNextptr();
        }
    }

    void printToFile(){
        Node<NODETYPE>* current = this->pHead;
        std::ofstream outfile;
        outfile.open("commands.csv",std::ios::trunc); //"std::ios::trunc" clears the content of the file initially
        if (outfile.is_open()) {
            //write stuff here.
            while (current->getNextptr()!= nullptr) {
                outfile << current->getData().getCommand() << "," << current->getData().getDescription() << "," << current->getData().getPoints() << endl;
                current = current->getNextptr();
            }
            if (current->getNextptr() == nullptr) {
                outfile << current->getData().getCommand() << "," << current->getData().getDescription() << "," << current->getData().getPoints() << endl;
            }
            
        }
        outfile.close();

        cout << "\nsuccessfully printed to the file\n";
    }

    Node<NODETYPE>* findNode(int position){
        Node<NODETYPE>* current = this->pHead;
        int counter = 0;

        while (current != nullptr) {
            if (counter == position) {
                return current;
            }
            counter++;
            current = current->getNextptr();
        }

        return nullptr;
    }

    string findRandomDescription(int number){
        string randomCommand = "";
        Node<NODETYPE>* randomNode = nullptr;

        randomNode = findNode(number);

        randomCommand = randomNode->getData().getDescription();

        return randomCommand;
    }

    // Function to get the current number of commands 
    int getNumCommands() const {
        return this ->numCommands; 
    }

    // Function to increment the count when a command is added 
    void incrementNumCommands() {
        this->numCommands++;
    }

    // Function to decrement the count when a command is removed
    void decrementNumCommands() {
        this->numCommands--;
    }


private:
    Node<NODETYPE>* pHead;
    void destroyList(){
        Node<NODETYPE>* pMem = this->pHead;
        Node<NODETYPE>* pCur = pMem;
        while (pMem!= nullptr){
            pCur = pMem;
            pMem = pMem->getNextptr();
            delete pCur;
            pCur = nullptr;
        }

        pMem = nullptr;
    }

    int numCommands; // Store the current number of commands 
};