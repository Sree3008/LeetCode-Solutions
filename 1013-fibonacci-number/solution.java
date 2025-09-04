class Solution {
    public int fib(int n) {
        int a=0;
        int b=1;
        int k=0;
        for(int i=0;i<=n;i++){
            k=a;
            int c=a+b;
            a=b;
            b=c;

        }
        return k;
    }
}
