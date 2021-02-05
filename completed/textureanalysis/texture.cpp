#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

void print_each(string i){
	cout << i << endl;
}

int main(int argc, char const *argv[])
{
	int n = 1;
	string delim = "*";
	string in;
	cin >> in;
	while(in.compare("END") != 0){
		cout << n << " ";
		std::vector<string> v;
		size_t start = in.find(delim)+delim.length();
		size_t end = in.find(delim,start);
		while(end != string::npos){
			v.push_back(in.substr(start,end - start));
			start = end + delim.length();
			end = in.find(delim,start);
		}
		//cout << v.size() << endl;
		//for_each(v.begin(),v.end(), print_each);
		int same = true;
		if (v.size() != 0){
			int len = v[0].length();
			for (int i = 1; i < v.size(); i++)
			{
				if (v[i].length() != len){
					same = false;
					break;
				}
			}
		}
		string out = (same) ? "EVEN" : "NOT EVEN";
		cout << out << endl;
		n++;
		cin >> in; 
	}
	return 0;
}