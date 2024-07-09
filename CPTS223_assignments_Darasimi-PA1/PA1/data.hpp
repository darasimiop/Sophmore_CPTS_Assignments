#include "PA1.hpp"
#pragma once
class Data {
public:
    Data(string Command = "", string Description = "", int Points=0){
        this->command = Command;
        this->description = Description;
        this->points = Points;   
    };
    //copy constructor
    Data(Data& copy){
        this->command = copy.command;
        this->description = copy.description;
        this->points = copy.points;
    };

    // getters
    string getCommand() const {
        return this->command;
    }

    string getDescription() const {
        return this->description;
    }

    int getPoints() const{
        return this->points;
    }

    // setters
    void setCommand(string newCommand){
        this->command = newCommand;
    }

    void setDescription(string newDescription){
        this->description = newDescription;
    }

    void setPoints(int newPoints){
        this->points = newPoints;
    }

private:
    string command;
    string description;
    int points;
};
