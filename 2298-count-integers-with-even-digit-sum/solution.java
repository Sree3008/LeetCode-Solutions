class Solution {
    public int countEven(int num) {
        int c=0;
        for(int i=1;i<=num;i++){
            int s=0;
            int t=i;
            while(t!=0){
                int m=t%10;
                s+=m;
                t/=10;
            }
            if(s%2==0){
                c++;
            }
        }
        
        return c;
    }
}
