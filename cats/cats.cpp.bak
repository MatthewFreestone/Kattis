#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
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
    int a, b, dist;
};

int main(){
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i){
        int m,c;
        scanf("%d %d", &m, &c);

        vector<int> parents(c+1);
        for (int j = 0; j < c+1; ++j){
            parents[j] = j;
        }

        vector<edge> edges;
        for (int j = 0; j < (c*(c-1)/2); ++j){
            int a,b, cost;
            scanf("%d %d %d", &a, &b, &cost);
            edges.push_back({a,b,cost});
        }
        sort(edges.begin(), edges.end(), [](edge a, edge b){return a.dist < b.dist;});

        int cats_connected = 1;
        for (auto [x, y, dist] : edges){
            if (find(parents, x) == find(parents, y)) continue;
            if (cats_connected == c) {
                break;
            }
            m -= dist + 1;
            cats_connected++;
            union_f(parents, x, y);
            if (m<0){
                printf("no\n");
                break;
            }
        }
        if (m>=0){
            printf("yes\n");
        }
    }

    return 0;
}