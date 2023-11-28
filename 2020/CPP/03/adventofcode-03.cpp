#include "adventofcode-03.h"

#include <iostream>
#include <cstring>

int adventofcode::countTrees(const vector<string>& data, int column, int row) {

    // counter for trees
    int trees = 0;

    // c for column to be checked
    int c = column;

    // l for rows
    int l = data[0].size() - 1;

    for (int r = row; r < data.size(); r += row) {

        if (data[r][c] == '#')
            trees ++;

        // check and adjust column if necessary 
        c = (c > (l - column)) ? ((c + column) - l - 1) : c + column;

    }

    return trees;
}

void adventofcode::part2(const vector<string>& data) {

    long s1 = countTrees(data, 1, 1);
    long s2 = countTrees(data, 3, 1);
    long s3 = countTrees(data, 5, 1);
    long s4 = countTrees(data, 7, 1);
    long s5 = countTrees(data, 1, 2);

    long solution = ((((s1 * s2) * s3) * s4) * s5);
    cout << "number of trees for part 2: " << solution << endl;
}

void adventofcode::part1(const vector<string>& data) {
    cout << "number of trees for part 1: " << countTrees(data, 3, 1) << endl;
}

bool adventofcode::inputFileExists() {
    bool ret = false;
    ifstream f(inputFileName);
    return f.good();
}

adventofcode::adventofcode(string year, string day) {

    // get data 
    if (!inputFileExists()) {
        string hostAddress = "https://adventofcode.com/" + year + "/day/" + day + "/input";
        string sessionID = "53616c7465645f5f3d8f075329f2c61abe7eef94accb8e55e9cc298e2a72dc12192eaa7129cc3742419d7d177ca0ce38";
        string command = "curl " + hostAddress + " -H \"Cookie: session=" + sessionID + "\" > " + inputFileName;
        system(command.c_str());
    }

    // read data
    vector<string> data = {};
    string line = "";
    ifstream fileId(inputFileName);

    if (fileId.is_open()) {

        while (getline(fileId, line))
        {
            data.push_back(line);
        }

    }

    fileId.close();

    // start
    part1(data);
    part2(data);

}

adventofcode::~adventofcode() {}

