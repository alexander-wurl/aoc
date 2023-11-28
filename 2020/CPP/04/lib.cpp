#include "lib.h"

void callFromLib() {
    std::cout << "call from lib!" << std::endl;
}

std::vector<std::string> SplitTextByDelimiter(std::string text, const std::string& delimiter) {
    std::vector<std::string> ret;

    // first finding of 'delimiter' ...
    int pos = text.find(delimiter);

    // ... indicates whether or not to loop
    while (pos > -1) {
        pos = text.find(delimiter);
        std::string s = text.substr(0, pos);
        ret.push_back(s);
        text = text.substr(pos + 1, text.length());
        pos = text.find(delimiter);
    }

    // remaining 'text' must be considered out of loop
    ret.push_back(text);

    return ret;
}

bool inputFileExists() {
    bool ret = false;
    std::ifstream f(inputFileName);
    return f.good();
}

std::vector<std::string> getData(std::string year, std::string day) {

    // get data 
    if (!inputFileExists()) {
        std::string hostAddress = "https://adventofcode.com/" + year + "/day/" + day + "/input";
        std::string sessionID = "53616c7465645f5f3d8f075329f2c61abe7eef94accb8e55e9cc298e2a72dc12192eaa7129cc3742419d7d177ca0ce38";
        std::string command = "curl " + hostAddress + " -H \"Cookie: session=" + sessionID + "\" > " + inputFileName;
        system(command.c_str());
    }

    // read data
    std::vector<std::string> data = {};
    std::string line = "";
    std::ifstream fileId(inputFileName);

    if (fileId.is_open()) {

        while (getline(fileId, line))
        {
            data.push_back(line);
        }

    } else {
        std::cout << "could not open " << inputFileName << std::endl;
    }

    fileId.close();

    return data;
}
