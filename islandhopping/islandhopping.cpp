#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;
int find(vector<int> &parents, int a){
    if (parents[a] == a){
        return a;
    }
    return parents[a] = find(parents, parents[a]);
}
void union_f(vector<int> &parents, int a, int b){
    parents[find(parents, a)] = find(parents, b);
}

struct edge {
    int a, b;
    double dist;
};

int main(){
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i){
        int m;
        scanf("%d", &m);
        vector<pair<float,float>> points(m);
        for (int j = 0; j < m; ++j){
            float a,b;
            scanf("%f %f", &a, &b);
            points[j] = {a,b};
        }
        vector<edge> edges;
        for (int j = 0; j < m; ++j){
            for (int k = j+1; k < m; ++k){
                float dist = (points[j].first - points[k].first)*(points[j].first - points[k].first) + (points[j].second - points[k].second)*(points[j].second - points[k].second);
                dist = sqrt(dist);
                edges.push_back({j,k,dist});
            }
        }
        sort(edges.begin(), edges.end(), [](edge a, edge b){return a.dist < b.dist;});

        vector<int> parents(m);
        for (int j = 0; j < m; ++j){
            parents[j] = j;
        }

        int islands_connected = 1;
        double cost = 0;
        for (auto [x, y, dist] : edges){
            if (find(parents, x) == find(parents, y)) continue;
            if (islands_connected == m) {
                break;
            }
            cost += dist;
            islands_connected++;
            union_f(parents, x, y);
        }
        printf("%.6f\n", cost);

    }
    return 0;
}