#ifndef __PROBING_HASH_H
#define __PROBING_HASH_H

#include <vector>
#include <stdexcept>
#include <cmath>  // Added for the use of sqrt function

#include "Hash.hpp"

using std::vector;
using std::pair;

enum EntryState {
    EMPTY = 0,
    VALID = 1,
    DELETED = 2
};

template<typename K, typename V>
class ProbingHash : public Hash<K,V> {
private:
    std::vector<std::pair<K, V>> table;
    std::vector<int> states;
    int numElements;

public:
    ProbingHash(int n = 11) : numElements(0), table(n), states(n, EMPTY) {
    }

    ~ProbingHash() {
        this->clear();
    }

    int size() override {
        return numElements;
    }

    V operator[](const K& key) override {
        int idx = hash(key);
        int originalIdx = idx;
        while (states[idx] != EMPTY) {
            if (states[idx] == VALID && table[idx].first == key) {
                return table[idx].second;
            }
            idx = (idx + 1) % table.size();
            if (idx == originalIdx) break;
        }
        throw std::out_of_range("Key not found");
    }

    bool insert(const std::pair<K, V>& pair) override {
        int idx = hash(pair.first);
        int originalIdx = idx;
        while (states[idx] == VALID && table[idx].first != pair.first) {
            idx = (idx + 1) % table.size();
            if (idx == originalIdx) return false;
        }
        table[idx] = pair;
        states[idx] = VALID;
        ++numElements;
        float load = static_cast<float>(numElements) / table.size();
        if (load > 0.75) {
            rehash();
        }
        return true;
    }

    void erase(const K& key) override {
        int idx = hash(key);
        int originalIdx = idx;
        while (states[idx] != EMPTY) {
            if (states[idx] == VALID && table[idx].first == key) {
                states[idx] = DELETED;
                --numElements;
                return;
            }
            idx = (idx + 1) % table.size();
            if (idx == originalIdx) return;
        }
    }

    void clear() override {
        table.clear();
        states.clear();
        table.resize(11);
        states.resize(11, EMPTY);
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
        return key % table.size();
    }

    void rehash() {
        int newSize = findNextPrime(2 * table.size());
        std::vector<std::pair<K, V>> newTable(newSize);
        std::vector<int> newStates(newSize, EMPTY);

        for (size_t i = 0; i < table.size(); ++i) {
            if (states[i] == VALID) {
                int idx = hash(table[i].first);
                while (newStates[idx] == VALID) {
                    idx = (idx + 1) % newSize;
                }
                newTable[idx] = table[i];
                newStates[idx] = VALID;
            }
        }
        
        table = newTable;
        states = newStates;
    }

    int findNextPrime(int n) {
        while (!isPrime(n)) {
            n++;
        }
        return n;
    }

    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;

        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
};

#endif //__PROBING_HASH_H
