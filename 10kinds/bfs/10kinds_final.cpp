#include<iostream>
#include<vector>
#include<stack>
#include<utility>
using namespace std;

class Graph
{
   int V;
   vector<int>* adjacent;  
   
   public:
      Graph(int v);
      void addEdge(int u, int v);
      bool* dfs(int v, int destination);
};

Graph::Graph(int V){
   this->V = V;
   adjacent = new vector<int>[V];
}

void Graph::addEdge(int u, int v){
   adjacent[u].push_back(v);
}

bool* Graph::dfs(int v, int destination){
   bool *visited = new bool[V];
   for (int i = 0; i < V; i++)
   {
      visited[i] = false;
   }

   stack<int> toVisit;
   toVisit.push(v);
   while (!toVisit.empty()){
       int curr = toVisit.top();
       toVisit.pop();
       visited[curr] = true;
       if (curr == destination){
          return visited;
       }
       for (auto i = adjacent[curr].begin(); i != adjacent[curr].end(); ++i){
           if (!visited[*i]){
               toVisit.push(*i);
           }
       }

   }
   
   return visited;
}





int main(void)
{
   ios::sync_with_stdio(false);
   cin.tie(NULL);
   
   int r,c;
   cin >> r >> c; 

   vector<int> *flat = new vector<int>[r*c];
   string in; 
   for (int i = 0; i < r; i++)
   {
      cin >> in;
      for (char c: in)
      {
         int a = c - '0';
         flat->push_back(a);
      }
      
   }

   Graph g(r*c);
   
   //optimize by skipping rows 
   for (int i = 0; i < flat->size(); i++) //check around
   {
      if (i % c != c-1 && flat->at(i) == flat->at(i+1)){ //add to the right
         g.addEdge(i,i+1);
         //cout << "Connected " << i << " and " << i+1 << " (right)" << endl;
      }
      if (i % c != 0 && flat->at(i) == flat->at(i-1)){ //add to the left
         g.addEdge(i,i-1);
         //cout << "Connected " << i << " and " << i-1  << " (left)" << endl;
      }
      if ((i - c) > 0 && flat->at(i) == flat->at(i-c)){ //add above
         g.addEdge(i,i-c);
      }
      if ((i + c) < (r*c) && flat->at(i) == flat->at(i+c)){ //add below 
         g.addEdge(i,i+c);
      }
   }

   int n;
   cin >> n;

   string output("");
   vector<pair<int,int>> points;
   vector<int> solved;
   for (int i = 0; i < n; i++){
        int x1,x2,y1,y2;
        cin >> y1 >> x1 >> y2 >> x2; //TODO scanf
        int sIndex = (x1-1) + c*(y1-1);
        int eIndex = (x2-1) + c*(y2-1);
        pair<int,int> pt = {sIndex, eIndex};
        points.push_back(pt);
        solved.push_back(-1);
   }

   for (int i = 0; i < points.size(); i++) 
   {
      //cout << "solved is " << solved.at(i) << endl;
      if (solved.at(i) != -1){
        if ((solved.at(i) == 1)){
            output += "decimal\n";
        }
        else{
            output += "binary\n";
        }
        continue;
      }

      
      
      pair<int,int> pt = points.at(i);
      int sIndex = pt.first;
      int eIndex = pt.second;

      bool success = false;

      bool* visited;
      if (sIndex != eIndex){
        visited = g.dfs(sIndex, eIndex);
        if (visited[eIndex]){
            success = true;
        }


        for (int k = i; k < points.size(); k++)
        {
            pair<int,int> curr = points.at(k);
            int first = curr.first;
            int second = curr.second;
            if (solved.at(k) == -1 && visited[first] && visited[second]){
                solved[k] = flat->at(first);
                //cout << "added cheat for " << first << " " << second << "\n";
                //cout << "solved[" << k <<"] is now " << solved[k] << "\n";
                //printf("added cheat for %i %i", first, second);
            }
        }
        
      }
      else{
         success = true;
      }

      if(success){
         if (flat->at(eIndex) == 1){
            output += "decimal\n";
         }
         else{
            output += "binary\n";
         }
      }
      else{
         output += "neither\n";
      }
      
   }
   cout << output;
   return 0;
}

//scanf/printf