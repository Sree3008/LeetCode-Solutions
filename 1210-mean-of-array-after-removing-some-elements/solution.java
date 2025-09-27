class Solution {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        int remove = arr.length / 20;
        double sum=0.0;
        int i=0;
        for(i=remove;i<arr.length-remove;i++){
            sum=sum+arr[i];
        }
        double total=arr.length-(2*remove);;
        double mean=sum/total;
        return mean;
    }
}
