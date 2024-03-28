/*
Rating: ~ 4.8 / 10
Link: https://open.kattis.com/problems/knapsack
*/

#include <bits/stdc++.h>
using std::cin;
using std::cout;
using std::endl;
using std::make_pair;
using std::pair;
using std::vector;
using std::ios_base;

typedef long ll;

void fast() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

const int MAX_SIZE = 2100;
long memo[MAX_SIZE][MAX_SIZE];
pair<int, int> prev[MAX_SIZE][MAX_SIZE];

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

        for (int i = 0; i <= n; ++i) {
            memo[i][0] = 0;
            prev[i][0] = make_pair(-1,-1);
        }
        for (int w = 0; w <= c; ++w) {
            memo[0][w] = 0;
            prev[0][w] = make_pair(-1,-1);
        }

        for (int i = 1; i <= n; ++i) {
            for (int w = 1; w <= c; ++w) {
                if (weights[i-1] > w) {
                    memo[i][w] = memo[i-1][w];
                    prev[i][w] = make_pair(i-1, w);
                }
                else {
                    long take = values[i-1] + memo[i-1][w - weights[i-1]];
                    long leave = memo[i-1][w];
                    if (take > leave) {
                        memo[i][w] = take;
                        prev[i][w] = make_pair(i-1, w-weights[i-1]);
                    }
                    else {
                        memo[i][w] = leave;
                        prev[i][w] = make_pair(i-1, w);
                    }
                }
            }
        }
    
        // cout << path << "\t" << memo[n][c] << endl;
        // cout << memo[n][c] << endl;

        vector<long> res;
        auto curr = make_pair(n,c);
        int i = curr.first;
        int w = curr.second;

        while (i != -1) {
            // cout << i << " " << w << endl;
            curr = prev[i][w];
            if (curr.second != w && curr.first != -1) {
                res.push_back(curr.first);
            }
            i = curr.first;
            w = curr.second;
        }

        // for (int i = 0; i <= n; ++i) {
        //     for (int w = 0; w <= c; ++w) {
        //         cout << memo[i][w] << " ";
        //     }
        //     cout << endl;
        // }
        // for (int i = 0; i <= n; ++i) {
        //     for (int w = 0; w <= c; ++w) {
        //         cout << "(" << prev[i][w].first << "," << prev[i][w].second << ") ";
        //     }
        //     cout << endl;
        // }

        cout << res.size() << endl;
        for (int i = res.size() - 1; i >= 0; i-- ){
            cout << res[i] << " ";
        }
        cout << endl;

        int t = 0;
        for (auto i: res) {
            t += values[i];
        }
        // if (t != memo[n][c]){
        //     cout << "BAD STUFF actual: " << t << ", expected: " << memo[n][c] << endl;
        // }

    };
    return 0;
}
