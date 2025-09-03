class Solution {
    public int lengthOfLastWord(String s) {
        String[] strarr=s.split(" ");
        String st=strarr[strarr.length-1];
        int n=0;
        char[] arr=new char[st.length()];
        for(int i=0;i<st.length();i++){
            arr[i]=st.charAt(i);
        }
        //System.out.print(arr.length);
        return arr.length;
    }
}
