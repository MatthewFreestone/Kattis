#include<iostream>
#include<set>
#include<vector>
using namespace std;
int main()
{
   int cases;
   cin >> cases;
   for (int i = 0; i < cases; i++)
   {
      int cities;
      cin >> cities;
      set<string> visited;
      for (int i = 0; i < cities; i++)
      {
         string in;
         cin >> in;
         visited.insert(in);
      }
      printf("%i\n",visited.size());
   }
   
   return 0;
}
