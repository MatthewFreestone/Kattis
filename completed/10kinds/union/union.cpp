#include<iostream>
#include<vector>
#include <string>
using namespace std;

int find(vector<int> &parents, int child) {
	if (parents[child] == child) {
		return child;
	}
	parents[child] = find(parents, parents[child]);
	return parents[child];
}
void unionF(vector<int> &parents, int x, int y) {
	int parentX = find(parents, x);
	int parentY = find(parents, y);
	parents[parentY] = parentX;
}

int main(int argc, char const* argv[])
{
	int r, c;
	cin >> r >> c;
	vector<int> parents(r * c);
	for (int i = 0; i < r * c; i++)
	{
		parents[i] = i;
	}
	vector<string> in_map(r);
	for (int i = 0; i < r; i++)
	{
		cin >> in_map[i]; //of length c
	}
	int n;
	cin >> n;
	vector<int[4]> points(n);
	for (auto& point : points) {
		//int a,b,c,d;
		//cin >> a >> b >> c >> d;
		cin >> point[0] >> point[1] >> point[2] >> point[3];
	}


	for (int row = 0; row < r; row++) {//r times
		for (int col = 0; col < c; col++) { //c times
			if (col != c - 1 && in_map[row][col] == in_map[row][col + 1]) {
				unionF(parents, row * c + col, row * c + col + 1);
			}
			if (col != 0 && in_map[row][col] == in_map[row][col - 1]) {
				unionF(parents, row * c + col, row * c + col - 1);
			}
			if (row != r - 1 && in_map[row][col] == in_map[row + 1][col]) {
				unionF(parents, row * c + col, (row + 1) * c + col);
			}
			if (row != 0 && in_map[row][col] == in_map[row - 1][col]) {
				unionF(parents, row * c + col, (row - 1) * c + col);
			}
		}
	}
	for (auto& point : points) {
		int r1 = point[0];
		int c1 = point[1];
		int r2 = point[2];
		int c2 = point[3];
		int sIndex = (c1 - 1) + c * (r1 - 1);
		int eIndex = (c2 - 1) + c * (r2 - 1);
		if (find(parents, sIndex) == find(parents, eIndex)) {
			printf("%s", (in_map[r1 - 1][c1 - 1] == '1') ? "decimal\n" : "binary\n");
		}
		else {
			printf("neither\n");
		}
	}
}