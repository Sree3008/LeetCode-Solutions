class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Character> list=new Stack<Character>();
        int c=0;
        for(char ch:s.toCharArray()){
            if(ch=='('){
                c++;
                list.push(ch);
            }
            else if(ch==')'){
                if(c>0){
                    c--;
                    list.push(ch);
                }
            }
            else{
                list.push(ch);
            }
        }
        StringBuilder res=new StringBuilder();
        for(int i=list.size()-1;i>=0;i--){
            char ch=list.get(i);
            if(ch=='(' && c-->0){
                continue;
            }
            res.append(ch);
        }
        return res.reverse().toString();
    }
}
