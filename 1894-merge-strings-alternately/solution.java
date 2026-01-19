class Solution {
    public String mergeAlternately(String word1, String word2) {
        // ArrayList<Character> list1=new ArrayList<>();
        // ArrayList<Character> list2=new ArrayList<>();
        String s="";
        if(word1.length()>word2.length()){
            for(int i=0;i<word2.length();i++){
                char ch=word1.charAt(i);
                char ch1=word2.charAt(i);
                s+=ch;
                s+=ch1;
            }
            for(int i=word2.length();i<word1.length();i++){
                char ch2=word1.charAt(i);
                s+=ch2;
            }
        }
        if(word2.length()>word1.length()){
            for(int i=0;i<word1.length();i++){
                char ch=word1.charAt(i);
                char ch1=word2.charAt(i);
                s+=ch;
                s+=ch1;
            }
            for(int i=word1.length();i<word2.length();i++){
                char ch2=word2.charAt(i);
                s+=ch2;
            }
        }
        if(word1.length()==word2.length()){
            for(int i=0;i<word2.length();i++){
                char ch=word1.charAt(i);
                char ch1=word2.charAt(i);
                s+=ch;
                s+=ch1;
            }
        }
        return s;
    }
}
