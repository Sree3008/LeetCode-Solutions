class Solution {
    public String maxSumOfSquares(int num, int sum) {
        int d=sum;
        if(sum>9*num) 
        return "";
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<num;i++){
            int di=Math.min(9,sum);
            sb.append(di);
            sum=sum-di;
        }
        return new String(sb);
    }
}
