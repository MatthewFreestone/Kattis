/*
Rating: ~ 4.8 / 10
Link: https://open.kattis.com/problems/knapsack
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void fast() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

int main() {
    fast();
    int c,n;
    while (scanf("%d %d", &c,&n) == 2)
    {
        vector<int> weights, values;
        int cn = n;
        while (cn--) {
            int v,w;
            scanf("%d %d", &v, &w);
            values.push_back(v);
            weights.push_back(w);
        }
        vector<vector<int>> memo;
        vector<vector<int>> path_memo;
        memo.assign(n, vector<int>(c+1, -1));
        path_memo.assign(n, vector<int>(c+1, 0));
        // function<pair<int,int>(int,int,int)>
        function<pair<int,int>(int,int,int)> dp = [&](int id, int remainingW, int path) -> pair<int,int> {
            if ((id == n) || (remainingW == 0)) return make_pair(0, path);
            int &ans = memo[id][remainingW];
            int &path_ans = path_memo[id][remainingW];
            if (ans != -1) return make_pair(ans, path); //dp step!
            if (weights[id] > remainingW) {
                // we can't take, so we move on
                auto resp = dp(id + 1, remainingW, path); 
                ans = resp.first;
                path_ans = resp.second;
                return resp;
            }
            auto resp1 = dp(id + 1, remainingW, path); // we don't take
            auto resp2 = dp(id+1, remainingW - weights[id], path ^ (1 << id)); // we take
            resp2.first += values[id];
            if (resp1 > resp2) {
                ans = resp1.first;
                path_ans = resp1.second;
                return resp1;
            }
            else {
                ans = resp2.first;
                path_ans = resp2.second;
                return resp2;
            }
        };
        dp(0, c, 0);
        int path = path_memo[0][c];
        // cout << path << "\t" << memo[0][c] << endl;
        cout << memo[0][c] << endl;
        // cout << n << c << endl;
        vector<int> res;
        // for (auto line: memo) {
        //     for (auto v: line) {
        //         cout << v << " ";
        //     }
        //     cout << endl;
        // }
        // for (auto line: path_memo) {
        //     for (auto v: line) {
        //         cout << v << " ";
        //     }
        //     cout << endl;
        // }
        for (int i = 0; path; i++) {
            int t = 1 << i;
            if (path & t) {
                res.push_back(i);
                path ^= t;
            }
        }
        cout << res.size() << endl;
        for (int node : res) {
            cout << node << " ";
        }
        cout << endl;

    };
    return 0;
}
