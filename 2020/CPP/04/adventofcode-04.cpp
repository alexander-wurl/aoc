#include "adventofcode-04.h"

bool adventofcode::CheckPassport(const string& id, const string& value) {
    bool valid = false;

    if (id.compare("byr") == 0) {
        // byr (Birth Year) - four digits; at least 1920 and at most 2002.
        valid = ((stoi(value) >= 1920) && (stoi(value) <= 2002)) ? true : false; 
    } else if (id.compare("iyr") == 0) {
        // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        valid = ((stoi(value) >= 2010) && (stoi(value) <= 2020)) ? true : false;
    } else if (id.compare("eyr") == 0) {
        // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        valid = ((stoi(value) >= 2020) && (stoi(value) <= 2030)) ? true : false;
    } else if (id.compare("hgt") == 0) {
        // hgt (Height) - a number followed by either cm or in:
            // If cm, the number must be at least 150 and at most 193.
            // If in, the number must be at least 59 and at most 76.
        string unit = value.substr(value.length() - 2, value.length());
        string number = value.substr(0, value.length() - 2);

        if (unit.compare("cm") == 0)
            valid = ((stoi(number) >= 150) && (stoi(value) <= 193)) ? true : false;
        else if (unit.compare("in") == 0)
            valid = ((stoi(number) >= 59) && (stoi(value) <= 76)) ? true : false;

    } else if (id.compare("hcl") == 0) {
        // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        string r_hcl = "(#([a-f0-9]){6})";

        // match
        if (std::regex_match(value, std::regex(r_hcl) ))
            valid = true;

    } else if (id.compare("ecl") == 0) {
        // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        string r_ecl = "((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))";

        // match
        if (std::regex_match(value, std::regex(r_ecl) ))
            valid = true;

    } else if (id.compare("pid") == 0) {
        // pid (Passport ID) - a nine-digit number, including leading zeroes.
        string r_pid = "([0-9]{9})";

        // match
        if (std::regex_match(value, std::regex(r_pid) ))
            valid = true;

    }

    return valid;
}

bool adventofcode::CheckPassports(const vector<string>& passports, bool check_id_values) {
    bool valid = false;

    // obgligatory passport ids
    vector<string> ids = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

    for (int j = 0; j < ids.size(); j++) {

        valid = false;

        // every check started with valid = false
        for (int i = 0; i < passports.size(); i++) {

            // for each id check match with given passport
            //cout << "check:" << passport[i].substr(0, 3) << " == " << ids[j] << std::endl;
            if (passports[i].substr(0, 3) == ids[j]) {
                valid = true;
                if (check_id_values)
                    valid = CheckPassport(ids[j], passports[i].substr(4, passports[i].length()));
            }

        }

        // (for every id) if id was not found then return false
        if (valid == false)
            return false;

    }

    return valid;
}



void adventofcode::Part1(const vector<string>& data) {
    // string vector for a passport
    vector<string> passports = {};

    // counter for valid passports
    int valid_passports = 0;
    
    for (int i = 0; i < data.size(); i++) {

        // check for empty line
        if ((data[i] == "") || ((i + 1) == data.size())) {

            // check
            if (CheckPassports(passports, false))
                valid_passports ++;

            // clear old data
            passports = {};
        } else {

            vector<string> p = SplitTextByDelimiter(data[i].c_str(), " ");

            for (int j = 0; j < p.size(); j++) {
                passports.push_back(p[j]);
            }
        }
    }

    cout << "valid passports for part 1: " << valid_passports << endl;

}

void adventofcode::Part2(const vector<string>& data) {

    // string vector for passports
    vector<string> passports = {};

    // counter for valid passports
    int valid_passports = 0;
    
    for (int i = 0; i < data.size(); i++) {

        // check for empty line
        if ((data[i] == "") || ((i + 1) == data.size())) {

            // check
            if (CheckPassports(passports, true))
                valid_passports ++;

            // clear old data
            passports = {};
        } else {

            vector<string> p = SplitTextByDelimiter(data[i].c_str(), " ");

            for (int j = 0; j < p.size(); j++) {
                passports.push_back(p[j]);
            }
        }
    }

    cout << "valid passports for part 2: " << valid_passports << endl;

}

adventofcode::adventofcode() {

}