/*
Rating: ~ 3.5 / 10
Link: https://open.kattis.com/problems/kattissquest
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
  int n;
  cin >> n;
  set<pair<int, int>> quests;
  while(n--)
  {
    string cmd;
    cin >> cmd;
    if (cmd == "add")
    {
      int e, g;
      cin >> e >> g;
      quests.insert(make_pair(e, g));
    }
    else
    {
      int x;
      cin >> x;
      ll gold = 0;
      while (x > 0 && quests.size() > 0)
      {
        auto it = quests.lower_bound(make_pair(x, 0));
        if (it == quests.end())
        {
          it--;
        }
        if (it->first <= x)
        {
          gold += it->second;
          x -= it->first;
          quests.erase(it);
        }
        else
        {
          if (it == quests.begin())
          {
            break;
          }
          else
          {
            it--;
          }
        }
      }
      cout << gold << "\n";
    }
  }
  return 0;
}
