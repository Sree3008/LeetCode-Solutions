class Solution {
    public int minAddToMakeValid(String s) {
        int c1=0;
        int c2=0;
        for(char i:s.toCharArray())
        {
            if(i=='('){
                c1++;
            }
            else{
                if(c1>0){
                    c1--;
                }
                else{
                    c2++;
                }
            }
        }
        return c1+c2;
    } 
}
