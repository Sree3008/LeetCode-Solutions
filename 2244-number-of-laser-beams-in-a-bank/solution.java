class Solution {
    public int numberOfBeams(String[] bank) {
        int prev=0;
        int res=0;
        for(String i:bank){
            int c=0;
            for(char j:i.toCharArray()){
                if(j=='1') c++;
            }
            if(c!=0){
                res=res+prev*c;
                prev=c;
            }
        }
        return res;
    }
}
