#include <map>
#include "TwitterData.hpp"
using namespace std;

int main(int argc, char *argv[])
{
    // Schema: UserName,Last,First,Email,NumTweets,MostViewedCategory
    string raw_data[5][6] = {{"rangerPower", "Smit", "Rick", "smitRick@gmail.com", "1117", "power lifting"},
                             {"kittyKat72", "Smith", "Kathryn", "kat@gmail.com", "56", "health"},
                             {"lexi5", "Anderson", "Alexis", "lexi5@gmail.com", "900", "education"},
                             {"savage1", "Savage", "Ken", "ksavage@gmail.com", "17", "president"},
                             {"smithMan", "Smith", "Rick", "rick@hotmail.com", "77", "olympics"}};
    TwitterData *twitter_data = new TwitterData[5];
    for (int i = 0; i < 5; ++i)
    {
        twitter_data[i].setUserName(raw_data[i][0]);
        twitter_data[i].setActualName(raw_data[i][2] + " " + raw_data[i][1]);
        twitter_data[i].setEmail(raw_data[i][3]);
        twitter_data[i].setNumTweets(stoi(raw_data[i][4]));
        twitter_data[i].setCategory(raw_data[i][5]);
    }


//Map Scenario 1: Search based on UserName

    //Create a new std::map: 
    std::map<std::string, TwitterData> twitterMap;

    // Insert all Twitter data into the std::map:
    for (int i = 0; i < 5; ++i) {
    twitterMap[twitter_data[i].getUserName()] = twitter_data[i];
}

    //Iterate through the std::map and print the key-value pairs
    for (const auto& entry : twitterMap) {
    std::cout << "Key: " << entry.first << ", Value: " << entry.second.print() << std::endl;
}

    //Find the person whose username is savage1 and print out the entire record
    auto it = twitterMap.find("savage1");
if (it != twitterMap.end()) {
    std::cout << "User savage1 found. Data: " << it->second.print() << std::endl;
} else {
    std::cout << "User savage1 not found." << std::endl;
}

    //Remove this person from the map
    if (it != twitterMap.end()) {
    twitterMap.erase(it);
}

//Map Scenario 2 for searching based on EmailAddress

    // Create a new std::map for EmailAddress
std::map<std::string, TwitterData> emailMap;

    //Insert Twitter data into the email-based map:
    for (int i = 0; i < 5; ++i) {
    emailMap[twitter_data[i].getEmail()] = twitter_data[i];
}

    //Iterate through the email-based map and print key-value pairs:
    for (const auto& entry : emailMap) {
    std::cout << "Key (Email): " << entry.first << ", Value: " << entry.second.print() << std::endl;
}

    //Find the person whose email is "kat@gmail.com" and print out the entire record:
    auto emailIt = emailMap.find("kat@gmail.com");
if (emailIt != emailMap.end()) {
    std::cout << "User with email 'kat@gmail.com' found. Data: " << emailIt->second.print() << std::endl;
} else {
    std::cout << "User with email 'kat@gmail.com' not found." << std::endl;
}

    //Remove this person from the email-based map:
    if (emailIt != emailMap.end()) {
    emailMap.erase(emailIt);
}

    


    return 0;
}