#include "lib.h" // 

#include <vector> // vector<string>
#include <iostream> // cout, endl, string
#include <regex> // regular expressions

using namespace std;

class adventofcode {

    public:
        adventofcode();
        void Part1(const vector<string>&);
        void Part2(const vector<string>&);

    private:
        bool CheckPassports(const vector<string>& passports, bool check_id_values);
        bool CheckPassport(const string& id, const string& value);

};
