#include<iostream>
#include<unordered_map>
#include<string>
#include<vector>

using namespace std;
int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    printf("%d %d", n, q);
    int base = 0;
    unordered_map<int, int> map;
    for (int i = 0; i < q; i++)
    {
        string s;
        scanf("%s", &s);
        cout << s << endl;
        cout << "Test" << endl;
        if (s == "SET"){
            int p, m;
            scanf("%d %d", &p, &m);
            map[p] = m;
        }
        else if (s == "PRINT"){
            int p;
            scanf("%d", &p);
            if (map.find(p) != map.end())
                printf("%d\n", map[p]);
            else
                printf("%d\n", base);
        }
        else {
            int p; 
            scanf("%d", &p);
            map = unordered_map<int, int>();
            base = p;
        }
    }
    cout << "Test" << endl;
    // flush output
    return 0;
}