class Solution {
    public int longestValidParentheses(String s) {
        int ma = 0,n=1;
        Stack<Integer> st = new Stack<>();
        st.push(-1);
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                st.push(i);
                n+=1;
            }
            else{
                st.pop();
                n-=1;
                if(n==0){
                    st.push(i);
                    n+=1;
                }
                ma = Math.max(ma,i-st.peek());
            }
        }
        return ma;
    }
}
