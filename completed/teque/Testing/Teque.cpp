#include <iostream>
#include <deque>
#include <string>
#include<vector>
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
		vector<int> to_vector();
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
int Teque::size(){
	return a.size() + b.size();
}
vector<int> Teque::to_vector(){
	vector<int> out; 
	for(int v: a){
		out.push_back(v);
	}
	for(int v: b){
		out.push_back(v);
	}
	return out; 
}
