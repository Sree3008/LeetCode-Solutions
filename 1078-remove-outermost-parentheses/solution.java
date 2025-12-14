class Solution {
    public String removeOuterParentheses(String s) {
        String res = "";
        boolean flag = false;
        int c = 0;
        for(char i:s.toCharArray()){
            if(i=='('){
                if(!flag){
                    flag = true;
                }
                else{
                    c++;
                    res+="(";
                }
            }else{
                if(c>0){
                    c--;
                    res+=")";
                }else{
                    flag = false;
                }
            }
        }
        return res;
    }
}
