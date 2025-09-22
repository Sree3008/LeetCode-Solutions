class Solution {
    public double findMaxAverage(int[] arr, int k) {
        double max=-1e9;
        for(int i=0;i<=arr.length-k;i++){
            int sum=0;
            for(int j=i;j<i+k;j++){
                sum=sum+arr[j];
            }
           double avg=(double)sum/k;
            max=Math.max(max,avg);
        }
        return (double)max;
    }
}
