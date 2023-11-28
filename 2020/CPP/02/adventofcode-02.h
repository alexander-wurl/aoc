#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class adventofcode {

public:

    adventofcode();
    ~adventofcode();

    void part1(string file_name);
    void part2(string file_name);

private:

    bool is_password_valid(string);
    bool is_password_valid2(string);
    vector<string> split_by_delimiter(string, string);
    int count_char_in_text(string, char);
    bool check_char_in_text(string text, char c, int pos1, int pos2);

};

