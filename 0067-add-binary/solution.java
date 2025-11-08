class Solution {
    public String addBinary(String a, String b) {
        String res = "";
        int n1 = a.length(),n2 = b.length(),c=0;
        if(n1>n2){
            for(int i = 0;i<n1-n2;i++)
                b = '0'+b;
            n2 = n1;
        }else{
            for(int i = 0;i<n2-n1;i++)
                a = '0'+a;
            n1 = n2;
        }
        for(int i=n1-1;i>=0;i--){
            int x=0;
            if(a.charAt(i)=='1'){
                x++;
            }
            if(b.charAt(i)=='1'){
                x++;
            }
            if(c==1){
                x++;
            }
            if(x==1){
                res='1'+res;
                c=0;
            }
            else if(x==2){
                res='0'+res;
                c=1;
            }else if(x==3){
                res='1'+res;
                c=1;
            }
            else{
                res='0'+res;
            }
        }
        if(c==1){
            res='1'+res;
        }
        return res;
    }
}
