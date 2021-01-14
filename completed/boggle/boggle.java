public class boggle {
    public static void main(String[] args){

        
    }
}

class TrieNode{
    private HashMap<Character, TrieNode> children;
    private String content;
    private isWord;

    public TrieNode() {
        children = new char[26]();
        isEndOfWord = false;
    }

}

public class Trie{
    TrieNode root; 
    //suck my cock ethan nguyen

    public Trie() {
        children = new char[26]();
        isEndOfWord = false;
    }
    
    public void insert(String word){
        TrieNode current = root;

        for (char l: word.toCharArray()){
            current = current.getChildren()
            

        }
        
    }

}