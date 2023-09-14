#include<bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
typedef unordered_set<int> si;
typedef unordered_map<int, vector<int>> edgemap;


bool CycleDetect(edgemap& edges,int v, si& on_stack, si& visited)
{
    on_stack.insert(v);
    visited.insert(v);
    for (const int x: edges[v])
    {
	if (visited.count(x) == 0)
	{
	    if (CycleDetect(edges, x, on_stack, visited))
	    {
	        return true;
	    }
	}
	if (on_stack.count(x) > 0)
	{
	    return true;
	}
    }
    on_stack.erase(v);
    return false;
}

void dfs(edgemap& edges, int v, vi& stack, si& visited)
{
    for (const int x: edges[v])
    {
	if (visited.count(x) == 0)
	{
	    dfs(edges, x, stack, visited);
	}
    }
    stack.push_back(v);
    visited.insert(v);
}

int main(){
    int sticks, lines;
    cin >> sticks >> lines;
    edgemap edges;
    while(lines--)
    {
        int start, end;
        cin >> start >> end;
	edges[start].push_back(end);
    }

    // check for cycle using tarjan's
    int node_index = 0;
    si on_stack; 
    si visited;
    for (const auto &[key, value] : edges)
    {
        if (visited.count(key) == 0)
	{
	    if (CycleDetect(edges, key, on_stack, visited))
	    {
	        cout << "IMPOSSIBLE" << endl;
		return 0; 
	    }
	}
    }

    //topological sort
    vi stack;
    si visited_topo;
    for (const auto &[key, value] : edges)
    {
	if (visited_topo.count(key) == 0)
	{
	    dfs(edges, key, stack, visited_topo); 
	}
    }
    for (int i = stack.size() - 1; i >= 0; i--)
    {
	cout << stack[i] << endl;
    }
    for (int i = 1; i < sticks+1; i++)
    {
	if (edges.count(i) == 0)
	{
	    cout << i << endl;
	}
    }
    return 0;
}
