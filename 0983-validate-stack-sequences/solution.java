class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> list=new Stack<>();
        int j=0;
        for(int i=0;i<pushed.length;i++){
                list.push(pushed[i]);
            while(!list.isEmpty()&&j<popped.length&&list.peek()==popped[j]){
                list.pop();
                j++;
            }
        } 
        return list.isEmpty(); 
    }
}
