/*
Rating: ~ 4.7 / 10
Link: https://open.kattis.com/problems/minspantree
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

typedef pair<int, int> pii;
typedef tuple<int, int, int> pqItem;

void fast()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

int main()
{
    fast();
    int n, m;
    while (1)
    {
        cin >> n >> m;
        if (n == 0)
            return 0;
        map<int, vector<pii>> edges;
        for (int i = 0; i < n; i++)
            edges[i] = vector<pii>();
        while (m--)
        {
            int s, t, w;
            cin >> s >> t >> w;
            edges[s].push_back({t, w});
            edges[t].push_back({s, w});
        }
        priority_queue<pqItem, vector<pqItem>, greater<pqItem>> pq;
        int total_weight = 0;
        int total_visited = 1;
        set<pair<int, int>> mst;
        vector<int> visited(n, 0);
        for (auto &[d, w] : edges[0])
        {
            pq.push({w, 0, d});
        }
        visited[0] = 1;
        while (!pq.empty())
        {
            auto [w, s, t] = pq.top();
            // cout << "Checking " << s << " " << t << " " << w << endl;
            pq.pop();

            if (visited[t] == 0)
            {
                // cout << "Taking " << s << " " << t << " " << w << endl;
                // add to mst
                visited[t] = 1;
                // make sure order is (x,y) s.t. x<y 
                mst.insert({min(s,t), max(s,t)});
                total_weight += w;
                total_visited += 1;

                // add neighbors
                for (auto [d, nw] : edges[t])
                {
                    if (visited[d] == 0)
                    {
                        // cout << "\tAdding " << t << " " << d << " " << nw << endl;
                        pq.push({nw, t, d});
                    }
                }
            }
        }
        if (total_visited < n)
        {
            cout << "Impossible" << endl;
        }
        else
        {
            cout << total_weight << endl;
            for (auto [s, t] : mst)
            {
                cout << s << " " << t << endl;
            }
        }
    }
    return 0;
}
