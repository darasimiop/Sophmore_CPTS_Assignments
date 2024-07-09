/*
 *  Separate chaining hashtable
 */

#ifndef __CHAINING_HASH_H
#define __CHAINING_HASH_H

// Standard library includes
#include <iostream>
#include <vector>
#include <list>
#include <stdexcept>
#include <cmath>

// Custom project includes
#include "Hash.hpp"

// Namespaces to include
using std::vector;
using std::list;
using std::pair;

using std::cout;
using std::endl;

//
// Separate chaining based hash table - derived from Hash
//
template<typename K, typename V>
class ChainingHash : public Hash<K,V> {
private:
 std::vector<std::list<std::pair<K, V>>> table; // Vector of lists to store key-value pairs
    int numElements; // To track the number of elements
public:
    ChainingHash(int n = 11) : table(n), numElements(0) {
        
    }

    ~ChainingHash() {
        this->clear();
    }

    int size() {
        return numElements;
    }

    V operator[](const K& key) override {
        int idx = hash(key);
        for (auto& it : table[idx]) {
            if (it.first == key) {
                return it.second;
            }
        }
        throw std::out_of_range("Key not found");
    }

    bool insert(const std::pair<K, V>& pair) override {
        int idx = hash(pair.first);
        for (auto& it : table[idx]) {
            if (it.first == pair.first) {
                return false; // Key already exists
            }
        }
        table[idx].push_back(pair);
        ++numElements;
        float load = static_cast<float>(numElements) / table.size();
        if (load > 0.75) {
            rehash();
        }
        return true;
    }

    void erase(const K& key) override {
        int idx = hash(key);
        for (auto it = table[idx].begin(); it != table[idx].end(); ++it) {
            if (it->first == key) {
                table[idx].erase(it);
                --numElements;
                return;
            }
        }
    }

    void clear() override {
        for (auto& lst : table) {
            lst.clear();
        }
        numElements = 0;
    }

    int bucket_count() override {
        return table.size();
    }

    float load_factor() override {
         return static_cast<float>(numElements) / table.size();
    }

private:
int hash(const K& key) {
        // A simple hashing function, modify according to your data type
        return key % table.size();
    }

    void rehash() {
        int newSize = findNextPrime(2 * table.size());
        std::vector<std::list<std::pair<K, V>>> newTable(newSize);
        for (auto& bucket : table) {
            for (auto& pair : bucket) {
                int idx = hash(pair.first, newSize);
                newTable[idx].push_back(pair);
            }
        }
        table = std::move(newTable);
    }

    int findNextPrime(int n)
    {
        while (!isPrime(n))
        {
            n++;
        }
        return n;
    }

    bool isPrime(int n)
    {
        if (n <= 1) return false;
        if (n <= 3) return true;

        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

   int hash(const K& key, int size) {
        return key % size;
    }

};

#endif //__CHAINING_HASH_H
