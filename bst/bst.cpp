/*
Rating: ~ 7.1 / 10
Link: https://open.kattis.com/problems/bst
*/

/*
Explanation:
If we keep an actual balanced BST (map) of nodes in the tree, we can have the log (n) time
Whenever we insert a node, we check what nodes we have before and after it already in tree
Because the keys are unique, one of the two (before and after) must be a leaf.
The deeper one is going to be the leaf. If they're equally deep, it doesn't matter.
Then, store the new node with its depth. 
*/

#include <bits/stdc++.h>
using namespace std;

void fast()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}


int main()
{
  fast();
  int n;
  cin >> n;

  map<int, int> node_to_depth;

  int val;
  cin >> val;
  n--;
  node_to_depth.emplace(val, 0);
  cout << 0 << endl;

  // This must not be int, it will wrong answer
  long long total = 0;
  while (n--)
  {
    cin >> val;
    // cout << "Placing " << val << endl;
    auto itBefore = node_to_depth.lower_bound(val);

    int curr_depth = -1;
    if (itBefore != node_to_depth.begin())
    {
      itBefore--;
      int key = itBefore->first;
      int depth = itBefore->second;
      // cout << "Lower node is " << key << " at depth " << depth << endl;
      curr_depth = depth + 1;
    }

    // check after 
    auto itAfter = node_to_depth.upper_bound(val);
    if (itAfter != node_to_depth.end())
    {
      int key = itAfter->first;
      int depth = itAfter->second;
      // cout << "Upper node is " << key << " at depth " << depth << endl;
      curr_depth = max(curr_depth, depth + 1);
    }
    // cout << "Placing node " << val << " at depth " << curr_depth << endl;
    node_to_depth.emplace(val, curr_depth);
    total += curr_depth;

    cout << total << endl;
  }
  return 0;
}
