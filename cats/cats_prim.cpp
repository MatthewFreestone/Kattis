#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;

#define all(x) (x).begin(), (x).end()

struct destedge {
    int d, w;
};

class cmp {
public:
    // Reverse order, makes pq a min heap
    bool operator()(destedge a, destedge b){
        return a.w > b.w;
    }
};

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int m,c;
        scanf("%d %d", &m, &c);
        unordered_map<int, vector<destedge>> edges;
        for (int j = 0; j < (c*(c-1)/2); ++j){
            int a,b, cost;
            scanf("%d %d %d", &a, &b, &cost);
            edges[a].push_back({b,cost});
            edges[b].push_back({a,cost});
        }
        int cats_connected = 0;
        priority_queue<destedge, vector<destedge>, cmp> pq;
        pq.push({0,0});
        vi visited(c+1, 0);
        while(!pq.empty()){
            auto [node, dist] = pq.top();
            pq.pop();
            if (visited[node]) continue;
            visited[node] = 1;
            cats_connected++;
            m -= dist + 1;
            if (cats_connected == c) break;
            for (auto [n, d] : edges[node]){
                if (visited[n] == 0)
                    pq.push({n, d});
            }
        }
        if (m>=0){
            printf("yes\n");
        }
        else {
            printf("no\n");
        }
    }
}