class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> st=new Stack<>();
        char[] arr=s.toCharArray();
        for(char i:arr){
            if(!st.isEmpty() && i==st.peek()){
                    st.pop();
            }
            else{
                st.push(i);
            }
        }
        String s1="";
        while(!st.isEmpty()){
            s1+=st.pop();
        }
        System.out.print(s1);
        char[] ch=s1.toCharArray();
        String s2="";
        for(int i=ch.length-1;i>=0;i--){
            s2+=ch[i];
        }
        return s2;
    }
}
