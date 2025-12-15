class Solution {
    public int sumofdigits(int n){
        int s=0;
        while(n!=0){
            int m=n%10;
            s+=m;
            n=n/10;
        }
        return s;
    }
    public int getLucky(String s, int k) {
        int num=0;
        for(char ch:s.toCharArray()){
            int val = ch - 'a' + 1;
            num += sumofdigits(val); 
        }
        for (int i = 1; i < k; i++) {
            num = sumofdigits(num);
        }
        return num;
    }
}
