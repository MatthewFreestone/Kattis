#include<iostream>
#include<list>
#include<vector>
#include<chrono>
using namespace std;

class Graph
{
   int V;
   list<int>* adjacent;  
   void recVisit(int v, bool visited[], vector<int>* contains);
   

   public:
      Graph(int v);
      void addEdge(int u, int v);
      vector<int> dfs(int v);
};

Graph::Graph(int V){
   this->V = V;
   adjacent = new list<int>[V];
}

void Graph::addEdge(int u, int v){
   adjacent[u].push_back(v);
}

void Graph::recVisit(int v, bool visited[], vector<int>* contains){
   visited[v] = true;
   contains->push_back(v);
   for (list<int>::iterator i = adjacent[v].begin(); i != adjacent[v].end(); ++i){
      if(!visited[*i]){
         recVisit(*i, visited, contains);
      }
   } 
   
}

vector<int> Graph::dfs(int v){
   vector<int> contains;
   //if (adjacent->size() != 0){
      bool *visited = new bool[V];
      for (int i = 0; i < V; i++)
      {
         visited[i] = false;
      }
      recVisit(v, visited, &contains);
   //}
   return contains;
}





int main(void)
{
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

      vector<int> contains;
      if (sIndex != eIndex){
         contains = g.dfs(sIndex);
      }
      else{
         contains = {eIndex};
      }

      //cout << "At " << sIndex << ", contains is size " << contains.size() << " : ";

      bool success = false;
      for (int i = 0; i < contains.size(); i++)
      {
         if (contains.at(i) == eIndex){
            success = true;
            break;
         }
      }

      if(success){
         if (flat->at(eIndex) == 1){
            output += "decimal\n";
            //cout << "decimal" << endl;
         }
         else{
            output += "binary\n";
            //cout << "binary" << endl;
         }
      }
      else{
         output += "neither\n";
         //cout << "neither" << endl;
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