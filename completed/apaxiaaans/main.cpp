#include<iostream>

using namespace std;


int main()
{
   string input;
   cin >> input;

   string out;
   out.append(input, 0, 1);
   for (int i = 1; i < input.length(); i++)
   {

      //ut.append(input, i, 1);
      if (input[i] != input[i-1]){
         out.append(input, i, 1);
      }
   }
   cout << out;
}
