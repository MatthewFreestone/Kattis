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
    int c,n;
    while (scanf("%d %d", &c,&n) != EOF)
    {
        vector<int> weights, values;
        int cn = n;
        while (cn--) {
            int v,w;
            cin >> v >> w;
            values.push_back(v);
            weights.push_back(w);
        }
        int memo[2001][2001]; // instead of allocating dynamically, just use biggest possible.
        memset(memo, -1, sizeof(memo));

        function<int(int,int)> dp;
        dp = [&](int id, int remainingW) {
            if ((id == n) || (remainingW == 0)) return 0;
            int &ans = memo[id][remainingW];
            if (ans != -1) return ans; //dp step!
            if (weights[id] > remainingW) return ans = dp(id + 1, remainingW);
            return ans = max(dp(id + 1, remainingW), values[id] + dp(id+1, remainingW - weights[id]));
        };
        int ans = dp(0, c);
        cout << ans << endl;
    }


    return 0;
}
