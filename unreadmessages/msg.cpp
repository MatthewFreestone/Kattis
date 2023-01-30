#include<iostream>
#include<vector>
using namespace std;
int main(int argc, char const *argv[])
{
	int n,m;
	cin >> n >> m;
	std::vector<int> people(n);
	for (int i = 0; i < people.size(); i++)
	{
		people[i] = 0;
	}

	for (int i = 0; i < m; i++)
	{
		int total = 0;
		for (int k = 0; k < people.size(); k++)
		{
			total += ++people[k];
		}

		int sent;
		cin >> sent;
		sent -= 1;
		total -= people[sent];
		people[sent] = 0;

		int out = total/people.size();
		cout << out << endl;
	}
}