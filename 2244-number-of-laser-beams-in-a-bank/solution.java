class Solution {
    public int numberOfBeams(String[] bank) {
        int prev = 0;
        int res = 0;
        for(String i:bank){
            int cu = 0;
            for(char j:i.toCharArray()){
                if(j=='1') cu++;
            }
            if(cu!=0){
                res+= prev*cu;
                prev = cu;
            }
        }
        return res;
    }
}
