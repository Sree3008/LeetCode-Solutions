class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> list=new Stack<>();
        for(String ch:tokens){ 
            if(ch.length()>1||Character.isDigit(ch.charAt(0))){
                list.push(Integer.parseInt(ch));
            }
            else{
                char c=ch.charAt(0);
                int x=list.pop();
                int y=list.pop();
                if(c=='+'){
                list.push(x+y); 
                } 
                else if(c=='-'){
                    list.push(y-x);
                }
                else if(c=='*'){
                    list.push(x*y);
                }
                else{
                    list.push(y/x);
                }
            }
            
        }
        return list.pop();
    }
}

