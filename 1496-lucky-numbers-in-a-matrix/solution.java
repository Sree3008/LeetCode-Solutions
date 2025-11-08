class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        int[] row=new int[matrix.length];
        int[] col=new int[matrix[0].length];
        ArrayList<Integer> list=new ArrayList<>();
        Arrays.fill(row,Integer.MAX_VALUE);
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                col[j]=Math.max(col[j],matrix[i][j]);
                row[i]=Math.min(row[i],matrix[i][j]);
            }
        }
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(row[i]==col[j]&&col[j]==matrix[i][j]){
                    list.add(matrix[i][j]);
                }
            }
        }
        return list;
    }
}
