/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/compoundwords
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  vector<string> words;
  string input;
  while (cin >> input) {
    // input can consist of multiple words space separated
    stringstream ss(input);
    string word;
    while (ss >> word) {
      words.push_back(word);
    }
  }
  set<string> compound;
  for (int i = 0; i < words.size(); i++) {
    for (int j = 0; j < words.size(); j++) {
      if (i != j) {
        compound.insert(words[i] + words[j]);
      }
    }
  }

  for (auto it = compound.begin(); it != compound.end(); it++) {
    cout << *it << endl;
  }
  return 0;
}
