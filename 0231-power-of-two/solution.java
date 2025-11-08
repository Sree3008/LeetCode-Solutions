class Solution {
    public boolean isPowerOfTwo(int n) {
        int x = 1;
        if((n>0) && (n&(n-1))==0) return true;
        return false;

    }
}
