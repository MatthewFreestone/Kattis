/*
Rating: ~ 3.5 / 10
Link: https://open.kattis.com/problems/kattissquest
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void fast() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

struct quest {
    int energy;
    int gold;
    int uuid;
};

inline bool operator<(const quest& left, const quest& right) {
    if (left.energy != right.energy)
    {
        // lower energy is left
        return left.energy < right.energy;
    }
    // if energy is equal, tiebreak with gold
    if (left.gold != right.gold)
        return left.gold < right.gold;
    return left.uuid < right.uuid;
}

int main() {
    fast();
    int n;
    cin >> n;
    set<quest> quests;
    int uid = 0;
    while(n--)
    {
        string cmd;
        cin >> cmd;
        if (cmd == "add")
        {
            int e, g;
            cin >> e >> g;
            quests.insert({e, g, uid++});
            //for (auto& [e,g,u ]: quests)
            //    cout << e << "," << g << "," << u  << " ";
            //cout << endl;
        }
        else
        {
            int x;
            cin >> x;
            ll gold = 0;
            while (x > 0 && quests.size() > 0)
            {
                //cout << "x is now " << x << endl;
                auto it = quests.lower_bound({x, (int)1e9, uid++});
                if (it == quests.end())
                {
                    it--;
                }
                if (it->energy <= x)
                {
                    gold += it->gold;
                    x -= it->energy;
                    quests.erase(it);
                }
                else
                {
                    if (it == quests.begin())
                    {
                        break;
                    }
                    else
                    {
                        it--;
                        gold += it->gold;
                        x -= it->energy;
                        quests.erase(it);

                    }
                }
            }
            cout << gold << "\n";
        }
    }
    return 0;
}
