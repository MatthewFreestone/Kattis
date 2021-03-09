#include<iostream>
#include<list>
#include<vector>
#include<chrono>
#include<algorithm>
using namespace std;

class Graph
{
   int V;
   list<int>* adjacent;  
   void recVisit(int v, bool visited[]);
   

   public:
      Graph(int v);
      void addEdge(int u, int v);
      bool* dfs(int v);
};

Graph::Graph(int V){
   this->V = V;
   adjacent = new list<int>[V];
   cout << "graph init" << endl;
}

void Graph::addEdge(int u, int v){
   adjacent[u].push_back(v);
}

void Graph::recVisit(int v, bool visited[]){
   //printf("visited %i \n", v);
   visited[v] = true;
   for (list<int>::iterator i = adjacent[v].begin(); i != adjacent[v].end(); ++i){
      if(!visited[*i]){
         recVisit(*i, visited);
      }
   } 
   
}

bool* Graph::dfs(int v){
   cout << "dfs start" << endl;
   bool *visited = new bool[V];
   for (int i = 0; i < V; i++)
   {
      visited[i] = false;
   }
   recVisit(v, visited);
   cout << "finished recvisit" << endl;
   return visited;
}





int main(void)
{
   ios::sync_with_stdio(false);
   cin.tie(NULL);
   
   int r,c;
   cin >> r >> c; 

   auto start = chrono::high_resolution_clock::now();

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

   for (int i = 0; i < n; i++)
   {
      int x1,x2,y1,y2;
      cin >> y1 >> x1 >> y2 >> x2;


      int sIndex = (x1-1) + c*(y1-1);
      int eIndex = (x2-1) + c*(y2-1);

      bool success = false;

      bool* visited;
      if (sIndex != eIndex){
         visited = g.dfs(sIndex);
         if (visited[eIndex]){
            success = true;
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
   auto stop = chrono::high_resolution_clock::now();
   chrono::duration<double> elapsed = stop-start;
   cout << "Time taken was " << elapsed.count() << " seconds\n";
   cout << output;
   return 0;
}


//optimize: keep track of 1s and 0s sections 
//stop when u see end 