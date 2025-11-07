class Solution {
    public boolean checkXMatrix(int[][] arr) {
        int n=arr.length;
        int m=arr[0].length;
        int b=0;
        int k=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(i==j||i==n-j-1){
                    if (arr[i][j] == 0) {
                        return false;
                    }
                }
                else{
                    if (arr[i][j] != 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
