class Solution {
    public String lexSmallest(String s) {
       String small=s;
        int n=s.length();
        for(int k=1;k<=n;k++){
            String fs=new StringBuilder(s.substring(0,k)).reverse().toString() + s.substring(k);
            String ls=s.substring(0,n-k)+ new StringBuilder(s.substring(n-k)).reverse().toString();
            if(fs.compareTo(small)<0){
                small=fs;
            }
            if(ls.compareTo(small)<0){
                small=ls;
            }
        }
        return small;
    }
}
