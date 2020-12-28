#include<iostream>
#include<vector>
using namespace std;

vector<int>* test(vector<int>* in){
   in->push_back(1);
   return in; 
}


int main(int argc, char const *argv[])
{
   vector<int>* data;
   data = new vector<int>;
   test(data);
   cout << data->size();
   return 0;
}

