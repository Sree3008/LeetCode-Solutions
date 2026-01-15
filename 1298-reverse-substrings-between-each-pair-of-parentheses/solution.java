class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> list=new Stack<Character>();
        for(char i:s.toCharArray()){
            if(i!=')'){
                list.push(i);
            }
            else{
                String str="";
                while(list.peek()!='('){
                    str+=list.pop();
                }
                list.pop();
                for(char j:str.toCharArray()){
                    list.push(j);
                }
            }
        }
        String res="";
        while(!list.isEmpty()){
            res=list.pop()+res;
        }
        return res;
    }
}
