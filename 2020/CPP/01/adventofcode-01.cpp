#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int* get2Number2020(vector<int> arr) {

  int* ret = new int[2];

  for (int i = 0; i < arr.size(); i++) {
    
    for (int j = i + 1; j < arr.size() - 1; j++) {
      
      if ((arr[i] + arr[j]) == 2020) {
        ret[0] = arr[i];
        ret[1] = arr[j];
      }

    }

  }

  return ret;

}

int* get3Number2020(vector<int> arr) {
  
  int* ret = new int[3];

  for (int i = 0; i < arr.size(); i++) {
    
    for (int j = i + 1; j < arr.size() - 1; j++) {
      
      for (int k = j + 1; k < arr.size() - 1; k++) {
      
        if ((arr[i] + arr[j] + arr[k]) == 2020) {
          ret[0] = arr[i];
          ret[1] = arr[j];
          ret[2] = arr[k];
        }

      }

    }
    
  }

  return ret;

}

int main () {
  string line;

  ifstream fileId ("input-01.txt");

  vector<int> arr;

  if (fileId.is_open()) {

    while (getline (fileId, line))
    {
      arr.push_back(stoi(line)); 
    }

    fileId.close();

    int* result1 = get2Number2020(arr);
    cout << "solution for part 1: " << result1[0] << " * " << (result1[1]) << " = " << (result1[0] * result1[1]) << endl;

    int* result2 = get3Number2020(arr);
    cout << "solution for part 2: " << (result2[0]) << " * " << (result2[1]) << " * " << result2[2] << " = " << (result2[0] * result2[1] * result2[2]) << endl;

  } else {
    cout << "Unable to open file";
    exit(-1);
  }

  return 0;
}
