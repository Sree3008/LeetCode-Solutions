class Solution {
    public int minLength(String s) {
        Stack<Character> list=new Stack<Character>();
        for(char ch:s.toCharArray()){
            if(!list.isEmpty()){
                char x=list.peek();
                if((x=='A' && ch=='B')||(x=='C' && ch=='D')){
                    list.pop();
                }
                else{
                    list.push(ch);
                }
            }
            else{
                list.push(ch);
            }
        }
        return list.size();
    }
}
