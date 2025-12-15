class Solution {
    public boolean isAcronym(List<String> words, String s) {
        String st="";
        for(int i=0;i<words.size();i++){
            String str=words.get(i);
            char[] ch=str.toCharArray();
            st+=ch[0];
        }
        if(st.equals(s)){
            return true;
        }
        return false;
    }
}
