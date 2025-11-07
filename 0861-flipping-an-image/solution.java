class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n=image.length;
        int m=image[0].length;
        int[][] img=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(image[i][m-1-j]==1){
                    img[i][j]=0;
                }
                else{
                    img[i][j]=1;
                }
            }
        }
        return img;
    }
}
