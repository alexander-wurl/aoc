#include "adventofcode-04.h"

int main() {

    vector<string> data = getData("2020", "4");

    adventofcode aoc;

    aoc.Part1(data);
    aoc.Part2(data);

    return 0;
}