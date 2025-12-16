class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> st=new Stack<Character>();
        char[] nums=s.toCharArray();
        for(char i:nums){
            if(i=='#'){
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
        char[] arr=s1.toCharArray();
        String s2="";
        for(int i=arr.length-1;i>=0;i--){
            s2+=arr[i];
        }
        

        Stack<Character> st1=new Stack<Character>();
        char[] num=t.toCharArray();
        for(char i:num){
            if(i=='#'){
                if(!st1.isEmpty()){
                    st1.pop();
                }
            }
            else{
                st1.push(i);
            }
        }
        String s11="";
        while(!st1.isEmpty()){
            s11+=st1.pop();
        }
        char[] arr1=s11.toCharArray();
        String s22="";
        for(int i=arr1.length-1;i>=0;i--){
            s22+=arr1[i];
        }
        return s2.equals(s22);
    }
}
