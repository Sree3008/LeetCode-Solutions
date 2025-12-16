class Solution {
    public String removeStars(String s) {
        Stack<Character> st=new Stack<Character>();
        char[] arr=s.toCharArray();
        for(char i:arr){
            if(i=='*'){
                if(!st.isEmpty()){
                    st.pop();
                }
            }
            else{
                st.push(i);
            }
        }
        String s1="";
        while(!st.isEmpty()){
            s1+=st.pop();
        }
        char[] ch=s1.toCharArray();
        String s2="";
        for(int i=ch.length-1;i>=0;i--){
            s2+=ch[i];
        }
        return s2;
    }
}
