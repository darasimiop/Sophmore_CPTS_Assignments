// code source: https://www.codesdope.com/blog/article/c-linked-lists-in-c-singly-linked-list/

#include "linked_list.hpp"
#include <fstream>
#include <ctime>
using std::fstream;

#define GAME_RULES 1
#define PLAY_GAME 2
#define LOAD_PREVIOUS_GAME 3
#define ADD_COMMAND 4
#define REMOVE_COMMAND 5
#define EXIT 6 


int main()
{
linked_list<Data> commandsList; // create an instance of my linked_list

//Load the initial commans and descriptions from the "commans.csv" file
commandsList.addData(); 


    // linked_list a;
    // a.add_node(1);
    // a.add_node(2);

    //---------------------[MENU Section]-------------------------- 
    int option = 0;
    cout << "Please select an option listed below:" <<endl;

string newCommand, newDescription; 
                int newPoints; 

                // Seed the random number genrator with the current time 
srand(static_cast<unsigned int>(time(nullptr)));
    
    while (option != EXIT){
        cout << "1. Game Rules" << endl; 
        cout << "2. Play Game" << endl; 
        cout << "3. Load Previous Game" << endl; 
        cout << "4. Add Command" << endl; 
        cout << "5. Remove Command" << endl; 
        cout << "6. Exit" << endl; 
        cout << ">> "; 

        cin >> option; 

        switch (option) {
            case GAME_RULES:
                 // Display game rules here 
            cout << "Game Rules:" << endl;
            cout << "1. You will be presented with Linux commands and descriptions." << endl;
            cout << "2. Your goal is to match the correct description to each command. " << endl;
            cout << "3. For each correct match, you earn 1 point, and for each incorrect match, you loose one point." << endl;
            cout << "4. The game continues until you reach a specified number of questions." << endl;
            cout << "5. You can save and load your progress usinf the menu options. " << endl;
            cout << "6. Have fun and test your Linux command knowledge!" << endl;
            break; 


          
            case PLAY_GAME:
                // Implement the game logic here 
                // Call functions from Linked_list calss to play the game 
            {
                int numQuestions; 
                int currentScore = 0; 

                // Get the current number of commands from the linked list
                int maxQuestionNumber = commandsList.getNumCommands(); 
                cout << "Max Questions are: " << maxQuestionNumber << endl;

                cout << "Enter the number of questions to play (between 5 and 30): ";
                cin >> numQuestions;

                // Validate numQuestions to ensure it's within the desired range

                if (numQuestions < 5 || numQuestions > 30) {
                    cout << "Invalid number of questions. Please choose between 5 and 30." << endl; 
                    break;
                }

                // Play the game loop 
                for (int i = 0; i < numQuestions; i++) {
                    int randomQuestionNumber = rand() % maxQuestionNumber; // Generate a random number;
                    string randomDescription = commandsList.findRandomDescription(randomQuestionNumber);

                    cout<< "Command " << (i + 1) << ": " << randomDescription << endl; 
                    cout << "Enter your answer (the Linux command): ";

                    string playerAnswer;
                    cin >> playerAnswer; 

                    // Find the correct command corresponding to the description
                    Node<Data>* currentNode = commandsList.getHeadptr();
                    string correctCommand = "" ;

                    while (currentNode != nullptr) {
                        if (currentNode->getData() .getDescription() == randomDescription) {
                            correctCommand = currentNode->getData() .getCommand(); 
                            break;
                        }
                        currentNode = currentNode->getNextptr(); 
                    }

                    // Check if the player's answer is correct 
                    if (playerAnswer == correctCommand) {
                        cout << "Correct! You earned 1 point." << endl; 
                        currentScore++;
                    } else {
                        cout << "Incorrect! The correct command was: " << correctCommand << endl;
                        currentScore--;
                    }
                }
            }
            
            break; 

            case LOAD_PREVIOUS_GAME: 
                // Load previous game (if any)
                // Call functions from Linked_list calss to load the game
                {
                int numQuestions; 
                int currentScore = 0; 

                // Get the current number of commands from the linked list
                int maxQuestionNumber = commandsList.getNumCommands(); 

                cout << "Enter the number of questions to play (between 5 and 30): ";
                cin >> numQuestions;

                // Validate numQuestions to ensure it's within the desired range

                if (numQuestions < 5 || numQuestions > 30) {
                    cout << "Invalid number of questions. Please choose between 5 and 30." << endl; 
                    break;
                }

                // Load the player's previous score from a file, if it exists
                ifstream scoreFile("player_score.txt");
                if (scoreFile) {
                    scoreFile >> currentScore; 
                    scoreFile.close(); 
                } else {
                    cout << "No previous game data found." << endl;
                }

                // Play the game loop (same as before)
                for (int i = 0; i < numQuestions; i++) {
                    int randomQuestionNumber = rand() % maxQuestionNumber; // Generate a random number;
                    string randomDescription = commandsList.findRandomDescription(randomQuestionNumber);

                    cout<< "Command " << (i + 1) << ": " << randomDescription << endl; 
                    cout << "Enter your answer (the Linux command): ";

                    string playerAnswer;
                    cin >> playerAnswer; 

                    // Find the correct command corresponding to the description
                    Node<Data>* currentNode = commandsList.getHeadptr();
                    string correctCommand = "" ;

                    while (currentNode != nullptr) {
                        if (currentNode->getData() .getDescription() == randomDescription) {
                            correctCommand = currentNode->getData() .getCommand(); 
                            break;
                        }
                        currentNode = currentNode->getNextptr(); 
                    }

                    // Check if the player's answer is correct 
                    if (playerAnswer == correctCommand) {
                        cout << "Correct! You earned 1 point." << endl; 
                        currentScore++;
                    } else {
                        cout << "Incorrect! The correct command was: " << correctCommand << endl;
                        currentScore--;
                    }
                }

                // Display the final score and save it to a file 
                 cout << "Game Over! Your final score: " << currentScore << endl;

                ofstream saveScoreFile("player_score.txt");
                if (saveScoreFile.is_open()) {
                    saveScoreFile << currentScore;
                    saveScoreFile.close();
                } else {
                    cout << "Failed to save the score." << endl;
                }

                break; // Move this 'break' inside the 'if (scoreFile)' block
            }
            
            

            case ADD_COMMAND:
            {
                // Allow the user to asd a new command and dscription 
                // Call functions from Linked_list calss to add a command
                

                // Prompt the user to enter the new command, description, and points 
                cout << "Enter the new command: "; 
                cin >> newCommand; 

                cout << "Enter the description for the new command: ";
                cin >> newDescription; 

                cout << "Enter the points for the new command: "; 
                cin >> newPoints; 

                // Create a new Data object with the entered information 
                Data newData(newCommand, newDescription, newPoints); 

                // Call a function from your linked_list class to ass the new command
                commandsList.insert(newData); 

                cout << "Command added sucessfully!" << endl; 

            break;
            }
            case REMOVE_COMMAND:
            {
                // Allow the user to remove a command 
                // Call functions from Linked_list calss to remove a command
                string commandToRemove;

                //Prompt the user to enter a command to remove
                cout << "Enter the command to remove: ";
                cin >> commandToRemove; 

                // Call a function from your linked_list class to remove the command
                int removalResult = commandsList.deleteNode(commandToRemove);
                
                if (removalResult == 0) {
                    cout << "Command not found. Nothing removed." << endl;
                } else {
                    cout << "Command removed successfully!" << endl;
                }
                break; 
            }

            case EXIT:
                //Save commands and descriptions back to "commands.csv"
                cout <<"Exiting the orogram." << endl; 
                break;

            default:
                cout << "Invalid option. Please choose a valid option." << endl;
                break;

        }
    }
   
return 0;
}