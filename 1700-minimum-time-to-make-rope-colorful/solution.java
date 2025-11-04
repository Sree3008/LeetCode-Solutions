class Solution {
    public int minCost(String colors, int[] neededTime) {
        Character[] arr=new Character[colors.length()];
        for(int i=0;i<colors.length();i++){
            arr[i]=colors.charAt(i);
        }
        int ans=0;
        for(int i=1;i<arr.length;i++){
            if(arr[i]==arr[i-1]){
                ans=ans+Math.min(neededTime[i],neededTime[i-1]);
                neededTime[i] = Math.max(neededTime[i], neededTime[i - 1]);

            }
        }
        return ans;
    }
}
