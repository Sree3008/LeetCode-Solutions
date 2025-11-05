class Solution {
    public double averageWaitingTime(int[][] cus) {
      long totalwaittime=0;
      int ideltime=1;
      for(int cust[]:cus){
        if(ideltime<=cust[0]){
            ideltime=cust[0]+cust[1];
        }
        else{
            ideltime=ideltime+cust[1];
        }
        totalwaittime+=(ideltime-cust[0]);
      }
      return (double)(totalwaittime/(double)cus.length);
    }
}
