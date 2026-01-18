class Solution {
    public int findTheWinner(int n, int k) {
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=1;i<=n;i++){
            list.add(i);
        }
        int id=0;
        for(int i=0;i<n-1;i++){
            id+=k-1;
            id=id%(n-i);
            list.remove(id);
        }
        return list.get(0);
    }
}
