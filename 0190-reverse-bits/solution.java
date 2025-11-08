class Solution {
    public int reverseBits(int n) {
        int res = 0,c = 0;
        while(n>0){
            if((n&1)==1)
                res|=1;
            res<<=1;
            n>>=1;
            c++;
        }
        while(c<31){
            res<<=1;
            c++;
        }
        return res;
    }
}
