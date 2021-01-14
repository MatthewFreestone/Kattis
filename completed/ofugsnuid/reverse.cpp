#include<iostream>
#include<vector>
using namespace std; 

int main(int argc, char const *argv[])
{
   cin.tie(NULL);

   int amnt;
   cin >> amnt;
   vector<int> nums; 
   string out = "";

   for (int i = 0; i < amnt; i++)
   {
      int in; 
      cin >> in; 
      nums.push_back(in);
   }

   for (int i = amnt-1; i > -1; i--)
   {
      cout << nums[i] << "\n";
      //out += nums[i];
      //out += "\n";
   }
   
   //cout << out; 
   

   return 0;
}
