class Solution {
    public String firstPalindrome(String[] words) {
        
        for(int i=0;i<words.length;i++){
            char[] ch=words[i].toCharArray();
            String w="";
            for(int j=ch.length-1;j>=0;j--){
                w=w+ch[j];
            }
            if(w.equals(words[i])){
                
                return words[i];
            }
        }
        return "";
    }
}
