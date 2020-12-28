#include<iostream>
using namespace std;

int main(void)
{
   int in = 0;
   string out = "";
   cin >> in;
   while (in != -1){
      int distance = 0;
      int last_hr = 0;
      for (int i = 0; i < in; i++){
         int mph, hr;
         cin >> mph >> hr;
         distance += mph * (hr - last_hr);
         last_hr = hr; 
      }
      out += to_string(distance) + " miles\n";
      cin >> in;
   }
   cout << out;
   return 0;
}
