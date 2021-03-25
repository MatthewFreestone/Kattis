import java.util.*;
class Boggle{
	private Trie dict;
   	private char[][] board;
	private TreeSet<String> foundWords;
	private ArrayList<Integer>[] adjList;
	private int V = 16;

	Boggle(Trie dict){
		board = new char[4][4];
		foundWords = new TreeSet<>();
		adjList = null;
		this.dict = dict;
	}

	private void loadBoggle(Scanner in){
		for (int i = 0; i < 4; i++){
			board[i] = in.next().toCharArray();
			// for (int j = 0; j < 4; j++){
   //          	board[i][j] = in.next();
   //      	}
      	}
      	adjList = new ArrayList[V];
		for (int i = 0; i < V; i++){
        	adjList[i] = new ArrayList<Integer>();
      	}
      	//fill in matrix 
      	for (int i = 0; i < V; i++){
			int[] xy = fromRM(i);
			int x= xy[0];
			int y= xy[1];
			int[] around = {-1,0,1};

			for (int dx : around){
				for (int dy: around){
				   if ((dx != 0 || dy !=0) && validIndex(x + dx, y + dy)){
				      adjList[i].add(toRM(x + dx, y + dy));
				   }
				}
			}
      	}
	}
	private boolean validIndex(int x, int y){
    	return (x >= 0 && y>=0 && x<4 && y<4);
   	}	

   	public TreeSet<String> getAllScorableWords(int minimumWordLength) {
    	foundWords = new TreeSet<String>();
     	for (int i = 0; i < V; i++){
        	boolean[] visited = new boolean[V];
        	ArrayList<Integer> path = new ArrayList<>();
        	path.add(i);
        	getScoreableDFS(i, visited, path,minimumWordLength);
      	}
      	return foundWords;
  	}
  	private void getScoreableDFS(int c, boolean[] visited, List<Integer> path, int minLen){
    	visited[c] = true;
    	String curString = pathToString(path);
    	if (!dict.containsPrefix(curString)){
       		visited[c] = false;
        	return;
      	}
      	if(curString.length() >= minLen && dict.containsWord(curString)){
        	foundWords.add(curString);
      	}
      	for (Integer i : adjList[c]){
         	if (!visited[i]){
            	path.add(i);
            	getScoreableDFS(i, visited, path,minLen);
            	path.remove(path.size()-1);
            	//path.remove(i); //used to be this; very slow
         	}
      	}
      	visited[c] = false;
   	}

   	private String pathToString(List<Integer> path){
      	String out = "";
      	for (int i: path){
      		int[] xy = fromRM(i);
       		out += board[xy[0]][xy[1]];
      	}
      	//System.out.println(out);
    	return out;
   	}

   	private int getScore(String word){
   		int len = word.length();
   		switch (len) {
   			case 3:
   				return 1;
   			case 4: 
   				return 1;
   			case 5:
   				return 2;
   			case 6: 
   				return 3;
   			case 7:
   				return 5;
   			case 8: 
   				return 11;
   			default:
   				throw new IllegalArgumentException();
   		}
   	}

	private int[] fromRM(int n){
		int[] out = new int[2];
		out[0] = n%4; //x
		out[1] = n/4; //y
		return out; 
   	}

   	private int toRM(int x, int y){
		return (y*4 + x);
   	}




	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Trie dict = new Trie();
		int d = in.nextInt();
		for (int i = 0; i < d; i++){
			dict.insert(in.next());
		}
		int n = in.nextInt();
		for (int i = 0; i < n; i++){
			Boggle b = new Boggle(dict);
			b.loadBoggle(in);
			TreeSet<String> words = b.getAllScorableWords(0);
			int totalScore = 0;
			for (String w : words){
				totalScore += b.getScore(w);
			}
			List<String> listWords = new ArrayList<String>();
			for(String w: words){
				listWords.add(w);
			}
			Collections.sort(listWords, (String a, String c) -> Integer.compare(c.length(),a.length()));
			System.out.println(totalScore + " " + listWords.get(0) + " " + words.size());

		}

	}
}

class Trie{
	
	TrieNode root;
 
	Trie(){
	   root = new TrieNode();
	}
 
	private class TrieNode{
	   TrieNode[] children = new TrieNode[26];
	   boolean leaf;
	   TrieNode(){
		  leaf = false;
	   }
	}
 
	public void insert(String wordIn){
	   String word = wordIn.toUpperCase(); 
	   TrieNode n = root;
	   for (char c : word.toCharArray()){
		  int l = letterIndex(c);
 
		  if (n.children[l] == null){
			 n.children[l] = new TrieNode();
		  }
 
		  n = n.children[l];
	   }
	   n.leaf = true;
	}
 
	private int letterIndex(char c){
	   return c - 'A';
	}
 
	public boolean containsWord(String wordIn){
	   String word = wordIn.toUpperCase(); 
	   TrieNode n = root;
	   for (char c : word.toCharArray()){
		  int l = letterIndex(c);
		  if (n.children[l] == null){
			 return false; 
		  }
		  n = n.children[l];
	   }
	   return n.leaf; //true if word ends there, false otherwise 
	}
 
	public boolean containsPrefix(String wordIn){
	   String word = wordIn.toUpperCase(); 
	   TrieNode n = root;
	   for (char c : word.toCharArray()){
		  int l = letterIndex(c);
		  if (n.children[l] == null){
			 return false; 
		  }
		  n = n.children[l];
	   }
	   return true; //true if word ends there, false otherwise 
	}
 
 }