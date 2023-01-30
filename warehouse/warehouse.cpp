#include<iostream>
#include<map>
#include<string>
#include<vector> 
#include <bits/stdc++.h> 
using namespace std;

bool cmp(pair<string, int>& a, pair<string, int>& b){
	if (a.second != b.second){
		return a.second > b.second;
	}
	else{
		int res = a.first.compare(b.first);
		if(res > 0){
			return false;
		}
		else{
			return true; 
		}
	}
}
int main(int argc, char const *argv[])
{
	int b;
	cin >> b; 

	for (int i = 0; i < b; i++)
	{
		map<string, int> inventory;
		int n;
		cin >> n; 
		for(int k = 0; k < n; k++){
			int c; 
			string s;
			cin >> s >> c; 
			if (inventory[s] == NULL){
				inventory[s] = c; 
			}
			else{
				inventory[s] += c; 
			}
			
		}
		vector<pair<string,int>> vect;

		for(auto it: inventory){
			vect.push_back(it);
		}
		sort(vect.begin(), vect.end(), cmp);


		cout << inventory.size() << endl;
		for(auto it: vect){
			cout << it.first << " " << it.second << endl;
		}
	}
	
}

