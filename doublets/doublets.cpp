#include <bits/stdc++.h>
using namespace std;
int main() {
    vector<string> words;
    string curr;
    while (true)
    {
        getline(cin, curr);
        if (curr=="")
        {
            break;
        }
        words.push_back(curr);
    }
    unordered_set<string> wordsSet;
    for (auto& w: words)
    {
        wordsSet.insert(w);
    }
    unordered_map<string, vector<string>> edges;

    auto getEdges = [&](string word){
        if (edges.count(word) != 0) return edges[word];
        vector<string> e;
        for (int i = 0; i < word.length(); i++)
        {
            string curr = word;
            for (int c = 'a'; c < 'z'; c++)
            {
                curr[i] = c;
                if (wordsSet.count(curr) != 0){
                    e.push_back(c);
                }
            }
        }
        return edges[word]=e;
    }
    unordered_map<string,string> prevs; 
    auto bfs = [&](string start,string stop){
        unordered_set<string> visited;
        deque<pair<string,string>> queue;
        queue.push_left({start, start});
        while (! queue.empty())
        {
            auto& [curr, prev] = queue.pop_right();
            if (visited.count(prev) != 0) continue;
            prevs[curr] = prev;
            for (auto& d : getEdges(curr))
            {
                if (d == stop)
                {
                    prevs[stop] = curr;
                    return;
                }
            }

        }
    };

    while(getline(cin, curr))
    {
        istringstream iss(curr);
        string to, from;
        iss >> to >> from;



    }
    return 0;
}

