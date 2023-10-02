/*
Rating: ~ 7.1 / 10
Link: https://open.kattis.com/problems/bst
*/

#include <bits/stdc++.h>
using namespace std;

class TreeNode {
  public:
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  int n;
  cin >> n;

  int val;
  cin >> val;
  n--;
  TreeNode root(val);
  cout << 0 << endl;

  int c = 0;
  while(n--)
  {
    cin >> val;
    TreeNode* curr = &root;
    int depth = 1;
    while(true)
    {
      if(val < curr->val)
      {
        if(curr->left == NULL)
        {
          curr->left = new TreeNode(val);
          break;
        }
        else
        {
          curr = curr->left;
        }
      }
      else
      {
        if(curr->right == NULL)
        {
          curr->right = new TreeNode(val);
          break;
        }
        else
        {
          curr = curr->right;
        }
      }
      depth++;
    }
    c += depth;
    cout << c << endl;

  }
  return 0;
}
