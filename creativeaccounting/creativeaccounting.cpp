#include<bits/stdc++.h>
using namespace std;
int main() {
    int n,l,h;
    cin >> n >> l >> h;
    vector<int> days;
    int i = n;
    while(i--) {
        int c;
        cin >> c;
        days.push_back(c);
    }
    vector<int> prefix(n+1);
    for (i = 1; i <= n; i++) {
        prefix[i] = prefix[i-1] + days[i-1];
        // cout << prefix[i] << " ";
    }
    auto rsq = [&](int s, int t) {
        int l = (s > 0) ? prefix[s] : 0;
        return prefix[t] - l;
    };
    cout << rsq(0, 1) << endl;
    cout << rsq(0, 3) << endl;
    cout << rsq(1, 3) << endl;
    int lowest = 1e9;
    int highest = 0;
    for (int segment_size = l; segment_size <= h; segment_size++) {
        for (int offset = 0; offset < segment_size; offset++) {
            // check this solution
            int total = 0;
            if (offset > 0) {
                total += rsq(0, offset) > 0 ? 1 : 0;
            }
            for (i = offset; i < n; i += segment_size){
                total += rsq(i, min(i+segment_size, n)) > 0 ? 1 : 0;
            }
            highest = max(highest, total);
            lowest = min(lowest, total);
        }
    }
    cout << lowest << " "  << highest << endl;
            


    return 0;

}
