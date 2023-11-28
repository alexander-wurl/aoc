#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

static const string inputFileName = "input.txt";

class adventofcode {

    public:
        adventofcode(string, string);
        ~adventofcode();

    private:
        bool inputFileExists();
        int countTrees(const vector<string>&, int, int);
        void part1(const vector<string>&);
        void part2(const vector<string>&);

};