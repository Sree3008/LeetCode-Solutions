class Solution {
    public int maxDepth(String s) {
        int c = 0,ma = 0;
        for(char i:s.toCharArray()){
            if(i=='('){
                c++;
                ma = Math.max(ma,c);
            }
            if(i==')'){
                c--;
            }
        }
        return ma;
    }
}
