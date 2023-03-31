#include<cstdio>
#include<unordered_map>

using namespace std;
int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    int base = 0;
    unordered_map<int, int> map;
    for (int i = 0; i < q; i++)
    {
        char s[500];
        scanf("%s", &s);
        if (s[0] == 'S'){
            int p, m;
            scanf("%d %d", &p, &m);
            map[p] = m;
        }
        else if (s[0] == 'P'){
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
    return 0;
}