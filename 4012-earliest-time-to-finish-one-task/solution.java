class Solution {
    public int earliestTime(int[][] tasks) {
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<tasks.length;i++){
            int sum=0;
            for(int j=0;j<tasks[0].length;j++){
                sum=sum+tasks[i][j];
            }
            list.add(sum);
        }
        int x=list.get(0);
        for(int i:list){
            if(i<x){
                x=i;
            }
        }
        return x;
    }
}
