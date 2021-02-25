#include<iostream>
#include<list>
#include<string>
using namespace std; 

int locate(list<int> stack, int target){
	int i = 0;
	for (int c: stack){
		if (c == target){
			stack.//HOW TO REMOVE?
			return i;
		}
		i++;
	}
	return -1; 
}
int main(int argc, char const *argv[]){
	int n; 
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		int m, r;
		string out; 
		cin >> m >> r;
		list<int> stack(m);
		int x = m;
		for(;x>0;x--){
			stack.push_back(x);
		}
		for (int i = 0; i < r; ++i)
		{
			int c;
			cin >> c;
			int index = locate(stack, c);
			int before = m-index-1;
			out += before + "\n";

		}



	}

}