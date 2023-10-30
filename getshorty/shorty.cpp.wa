#include<iostream>
#include<utility>
#include<vector>
#include<climits>
using namespace std;

int maxFactor(vector<double>* dist, vector<bool>* splSet, int n){
	double max = INT_MIN, max_index;
	//cout << "Dist array: " << dist->at(0) << " " << dist->at(1) << " " << dist->at(2) << " " << dist->at(3) << endl;
	for (int i = 0; i < n; ++i)
	{
		if (splSet->at(i) == false && dist->at(i) > max){
			max = dist->at(i);
			max_index = i;
		}
	}
	//cout << "Max was " << max << " at " << max_index << endl; 

	return max_index;
}


int main(int argc, char const *argv[]) {
	int n,m; //m is path count, n is nodes
	cin >> n >> m;
	while(n != 0 && m != 0){
		vector<double> dist(n, INT_MIN); //initialize n spots as MIN
		vector<bool> splSet(n, false);
		//vector<pair<int,double>> adj[10000];
		vector<vector<pair<int,double>>> adj(n);
		for (int i = 0; i < m; ++i) //paths
		{
			int x,y;
			double f;
			cin >> x >> y >> f; 
			pair<int,double> a (y,f);
			adj[x].push_back(a);
			pair<int,double> b (x,f);
			adj[y].push_back(b);
		}

		dist[0] = 1; //path to start from start

		for (int i = 0; i < n-1; ++i)
		{
			int u = maxFactor(&dist, &splSet, n);
			//cout << "Max factor was " << u << endl;
			splSet[u] = true; //settle this one

			for (pair<int,double> p: adj[u])
			{
				int to = p.first;
				double weight = p.second;
				if (splSet[to] == false && dist[i] != INT_MIN 
					&& dist[i] * weight > dist[to])
				{
					dist[to] = dist[i] * weight;
				}
			}
		}
		//cout << "Answer: ";
		printf("%.4f\n", dist[n-1]);

		// delete(paths);
		// delete(costs);
		// delete(adj);
		cin >> n >> m;
	}


	return 0;
}