#include "adventofcode-02.h"

adventofcode::adventofcode() {}

adventofcode::~adventofcode() {}

bool adventofcode::is_password_valid(string line) {
  bool ret = false;
  vector<string> l = split_by_delimiter(line, " ");  
  vector<string> n = split_by_delimiter(line, "-");
  int n_min = stoi(n[0]);
  int n_max = stoi(n[1]);
  const char* c = l[1].c_str();
  string password = l[2];
  int count = count_char_in_text(password, c[0]);

  if ((count >= n_min) && (count <= n_max))
    ret = true;

  return ret;
}

bool adventofcode::is_password_valid2(string line) {
  vector<string> l = split_by_delimiter(line, " ");  
  vector<string> n = split_by_delimiter(line, "-");
  int pos1 = stoi(n[0]);
  int pos2 = stoi(n[1]);
  string t = l[1];
  const char* c = t.c_str();
  string password = l[2];
  return check_char_in_text(password, c[0], pos1, pos2);
}

int adventofcode::count_char_in_text(string text, char c) {
  int ret = 0;
  int pos = text.find(c);

  while (pos != -1) {
    text = text.substr(pos + 1, text.length());
    pos = text.find(c);
    ret++;
  }

  return ret;
}

bool adventofcode::check_char_in_text(string text, char c, int pos1, int pos2) {

  if ((text[pos1-1] == c) && (text[pos2-1] != c)) {
    return true;
  }

  if ((text[pos1-1] != c) && (text[pos2-1] == c)) {
    return true;
  }

  return false;
}

vector<string> adventofcode::split_by_delimiter(string text, string delimiter) {
  vector<string> ret;

  int pos = 0;

  do {
    pos = text.find(delimiter);
    string s = text.substr(0, pos);
    ret.push_back(s);
    text = text.substr(pos + 1, text.length());
    pos = text.find(delimiter);
  } while (pos > -1);
  ret.push_back(text);
  
  return ret;
}

void adventofcode::part1(string file_name) {
  string line;
  int valid_passwords = 0;
  ifstream fileId ("input-02.txt");

  if (fileId.is_open()) {

    while (getline(fileId, line))
    {
      if (is_password_valid(line))
        valid_passwords++;
    }

    fileId.close();
    cout << "valid passwords for part 1: " << valid_passwords << endl;

  } else {
    cout << "Unable to open file" << endl;
  }

}

void adventofcode::part2(string file_name) {
  string line;
  int valid_passwords = 0;
  ifstream fileId ("input-02.txt");

  if (fileId.is_open()) {

    while (getline(fileId, line))
    {
      if (is_password_valid2(line))
        valid_passwords++;
    }

    fileId.close();
    cout << "valid passwords for part 2: " << valid_passwords << endl;

  } else {
    cout << "Unable to open file" << endl;
    exit(-1);
  }

}