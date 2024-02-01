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
    vector<int> prefix(n);
    prefix[0] = days[0];
    for (i = 1; i < n; i++) {
        prefix[i] = prefix[i-1] + days[i];
        // cout << prefix[i] << " ";
    }
    auto rsq = [&](int s, int t) {
        if (s == 0) return prefix[t];
        return prefix[t] - prefix[s-1];
    };
    int lowest = 1e9;
    int highest = 0;
    for (int segment_size = l; segment_size <= h; segment_size++) {
        for (int offset = 0; offset < segment_size; offset++) {
            // check this solution
            int total = 0;
            int i = offset;
            while (true)
            {
                if (i == 0) {
                    i += segment_size;
                    continue;
                }
                int left = max(i - segment_size, 0);
                int right = min(i, n);
                total += rsq(left, right-1) > 0 ? 1 : 0;
                if (i >= n) break;
                i += segment_size;
            }
            highest = max(highest, total);
            lowest = min(lowest, total);
        }
    }
    cout << lowest << " "  << highest << endl;
    return 0;
}