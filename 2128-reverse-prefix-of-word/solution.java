class Solution {
    public String reversePrefix(String word, char ch) {
        Stack<Character> st = new Stack<>();
        int i,n=word.length();
        for(i=0;i<word.length();i++){
            st.push(word.charAt(i));
            if(word.charAt(i)==ch){
                break;
            }
        }
        if(i<n){
            String res = "";
            while(!st.empty()){
                res+=st.pop();
            }
            res+= word.substring(i+1);
            return res;
        }
        return word;
    }
}
