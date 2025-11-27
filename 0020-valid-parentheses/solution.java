class Solution {
    public boolean isValid(String str) {
        Stack<Character> st=new Stack<>();
        for(char ch:str.toCharArray()){
            if(ch=='('||ch=='['||ch=='{'){
                st.push(ch);
            }
            
            if(ch==')'||ch=='}'||ch==']'){
                if(st.isEmpty()) return false;
                char top=st.pop();
                if(ch==')'&&top!='(' ||
                ch==']'&&top!='[' ||
                ch=='}'&&top!='{'){
                    return false;
                }
            }
        } 
        return st.isEmpty();
    }
}
