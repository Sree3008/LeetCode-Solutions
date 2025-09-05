class Solution {
    public String reverseOnlyLetters(String s3) {
         char s1[]=s3.toCharArray();
        int left=0;
        int right=s1.length-1;
        String s="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
        while(left<right){
            while(left<right&& s.indexOf(s1[left])==-1){
                left++;
            }
            while(left<right&&s.indexOf(s1[right])==-1){
                right--;
            }
            char temp=s1[left];
            s1[left]=s1[right];
            s1[right]=temp;
            left++;
            right--;
        }
        return new String(s1);
    }
}
