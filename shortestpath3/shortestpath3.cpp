/*
Rating: ~ 4.7 10
Link: https://open.kattis.com/problems/shortestpath3
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void fast() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}
struct edge {
    int source;
    int dest;
    int weight;
};


int main() {
    fast();
    while (true)
    {
        int n,m,q,s;
        cin >> n >> m >> q >> s;
        if (n == 0){
            // n should be >= 1, so this is a valid check
            break;
        }
        //cout << "starting case with n = " << n << endl;
        vector<edge> edges;
        int cm = m;
        while (cm--){
            int u,v,w;
            cin >> u >> v >> w;
            edges.push_back({u,v,w});
        }
        vector<int> queries;
        while (q--){
            int c;
            cin >> c;
            queries.push_back(c);
        }

        vector<int> distances(n, 1e9);
        distances[s] = 0;
        // |V| - 1 goes
        for (int i = 1; i < n; i++){
            // iterate over edges
            for (int j = 0; j < m; j++){
                auto &[u, v, w] = edges[j];
                if (distances[u] != 1e9 && distances[u] + w < distances[v]){
                    distances[v] = distances[u]+w;
                }

            }
        }
        // Do another |V|-1 goes to get the negative bits
        for (int i = 1; i < n; i++){
            // iterate over edges
            for (int j = 0; j < m; j++){
                auto &[u, v, w] = edges[j];
                if (distances[u] != 1e9 && distances[u] + w < distances[v]){
                    distances[v] = -1e9;
                }

            }
        }
        for (vector<int>::iterator it = queries.begin(); it != queries.end(); ++it){
            int c = distances[*it];
            if (c == 1e9){
                cout << "Impossible" << endl;
            }
            else if (c == -1e9){
                cout << "-Infinity" << endl;
            }
            else{
                cout << c << endl;
            }
        }
        cout << endl;

    }

    return 0;
}
