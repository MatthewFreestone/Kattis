#include<iostream>
#include<string>
using namespace std;

int factorial(int n){
	if (n == 1){
		return 1;
	}
	return n * factorial(n-1);
}

int main(int argc, char const *argv[])
{
	int n;
	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		int f;
		cin >> f;
		int ans = factorial(f);
		//cout << ans << endl;
		string strAns = to_string(ans);
		cout << strAns.at(strAns.length()-1) << endl;

	}
	return 0;
}
