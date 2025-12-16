class Solution {
    public int calPoints(String[] op) {
        Stack<Integer> st=new Stack<>();
        for(int i=0;i<op.length;i++){
            if(op[i].equals("C")){
                if(!st.isEmpty()){
                    st.pop();
                }
            }
            else if(op[i].equals("D")){
                if(!st.isEmpty()){
                    int y=st.peek();
                    st.push(y*2);
                }
            }
            else if(op[i].equals("+")){
                if(!st.isEmpty() && st.size()>1){
                    int y=st.pop();
                    int z=st.peek();
                    st.push(y);
                    st.push(y+z);
                }
            }
            else{
                st.push(Integer.parseInt(op[i]));
            }
        }
        int sum=0;
        while(!st.isEmpty()){
            sum+=st.pop();
        }
        return sum;
    }
}
