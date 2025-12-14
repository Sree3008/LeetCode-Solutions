class Solution {
    public String removeStars(String s) {
        Stack<Character> st = new Stack<>();
        for(char i:s.toCharArray()){
            if(i=='*'){
                if(!st.empty())
                    st.pop();
            }
            else{
                st.push(i);
            }
        }
        String res = "";
        while(!st.empty())
            res=st.pop()+res;
        return res;
    }
}
