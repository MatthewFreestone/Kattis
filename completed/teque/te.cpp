#include <iostream>
#include <deque>
#include <string>
#include <stdio.h>
using namespace std;

class Teque {
	int middle; 
	deque<int> a, b;
	public:
		Teque();
		void push_front(int x);
		void push_back(int x);
		void push_middle(int x);
		int get(int x);
		int size();
};

Teque::Teque(){
	a = deque<int>(0);
	b = deque<int>(0);
}
void Teque::push_front(int x){
	a.push_front(x);
	if (a.size()-1 > b.size()){ //if a is now 2 bigger than b 
		b.push_front(a[a.size()-1]);
		a.pop_back(); //make equal size
	}
}
void Teque::push_back(int x){
	b.push_back(x);
	if (b.size() > a.size()){ //if b is now 1 bigger than a
		a.push_back(b[0]);
		b.pop_front(); // make a the longer deque
	}
}
void Teque::push_middle(int x){
	if (a.size() > b.size()){ //if a is 1 bigger than b 
		b.push_front(x); // make both the same size
	}
	else{ //if a and b are equal 
		a.push_back(x); //make a longer
	}
}
int Teque::get(int x){
	if (x < a.size()){
		return a[x];
	}
	else{
		return b[x-a.size()];
	}
}






int main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	Teque t;
	for (int i = 0; i < n; i++)
	{
		char temp[20];
		int x;
		scanf("%s %d", &temp, &x);
		string cmd = temp;
		if (cmd == "push_front"){
			t.push_front(x);
		}
		else if(cmd == "push_back"){
			t.push_back(x);
		}
		else if (cmd == "push_middle"){
			t.push_middle(x);
		}
		else if(cmd == "get"){
			printf("%d\n", t.get(x));
		}
		else{
			cout << "Invalid Input" << endl; 
			continue; //should never call
		}
	}

	return 0;
}