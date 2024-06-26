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
        memo.assign(n, vector<int>(c+1, -1));
        function<int(int,int)> dp = [&](int id, int remainingW)  {
            if ((id == n) || (remainingW == 0)) return 0;
            int &ans = memo[id][remainingW];
            if (ans != -1) return ans; //dp step!
            if (weights[id] > remainingW) {
                // we can't take, so we move on
                return ans = dp(id + 1, remainingW); 
            }
            int pos1 = dp(id + 1, remainingW); // we don't take
            int pos2 = values[id] + dp(id+1, remainingW - weights[id]); // we take
            return ans = max(pos1,pos2);
        };
        int res = dp(0, c);
        // cout << res << endl;

        // for (int i = 0; i < n; ++i) {
        //     for (int w = 0; w <= c; ++w) {
        //         cout << memo[i][w] << " ";
        //     }
        //     cout << endl;
        // }

        vector<int> path;
        function<void(int,int)> print_dp = [&](int id, int remW) {
            if ((id == n) || (remW == 0)) return;
            if (dp(id + 1, remW) != dp(id, remW)) {
                path.push_back(id);
                print_dp(id+1, remW - weights[id]);
            }
            else {
                print_dp(id+1, remW);
            }

        };
        print_dp(0, c);
        cout << path.size() << endl;
        for (int node : path) {
            cout << node << " ";
        }
        cout << endl;

        int t = 0;
        for (auto i: path) {
            t += values[i];
        }
        if (t != res){
            cout << "BAD STUFF: " << t << " " << res << endl;
        }

    };
    return 0;
}
