#include <iostream>
#include <fstream>
#include <vector>


static const std::string inputFileName = "input.txt";

/* test */
void callFromLib();

/* split text by given delimiter */
std::vector<std::string> SplitTextByDelimiter(std::string text, const std::string& delimiter);

/* - parameter year and day needed, for e.g. "2020", "4" */
/* - 'getData' fetches data from server 'adventofcode.com' if not found file 'input.txt' in local working dir */
/* - data then will be loaded from file, as well as stored and returned with help of a string vector */
std::vector<std::string> getData(std::string year, std::string day);

/* check if 'inpufFileName' exists */
bool inputFileExists();
