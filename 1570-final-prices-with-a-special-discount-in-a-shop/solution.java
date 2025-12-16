class Solution {
    public int[] finalPrices(int[] prices) {
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<prices.length;i++){
            int x=0;
            boolean b=false;
            for(int j=i+1;j<prices.length;j++){
                if(prices[i]>=prices[j]){
                    b=true;
                    x=prices[i]-prices[j];
                    break;
                }
            }
            if(b){
            list.add(x);
            }
            else{
                list.add(prices[i]);
            }
        }
        int[] arr=new int[list.size()];
        for(int i=0;i<arr.length;i++){
            arr[i]=list.get(i);
        }
        return arr;
    }
}
