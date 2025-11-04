class Solution {
    public String simplifyPath(String path) {
        String[] arr=path.split("/+");
        Stack<Object> st=new Stack<>();
        for(String i:arr){
            if(i.equals("")||i.equals(".")){
                continue;
            }
            else if(i.equals("..")){
            if(!st.isEmpty()){
                st.pop();
            }
            }
            else{
                st.push(i);
            }
        }
        String s="";
        while(!st.isEmpty()){
            s="/"+st.pop()+s;
        }
        return s.isEmpty()?"/":s;
    }
}
