class Solution {
    public boolean isAnagram(String s, String t) {
        char[] arr=new char[s.length()];
        char[] arr1=new char[t.length()];
        for(int i=0;i<s.length();i++){
            arr[i]=s.charAt(i);
        }   
        for(int j=0;j<t.length();j++){
            arr1[j]=t.charAt(j);
        }
        Arrays.sort(arr);
        Arrays.sort(arr1);
        boolean b=true;
        if(arr.length==arr1.length){
            for(int i=0;i<arr.length;i++){
            if(arr[i]!=arr1[i]){
                b=false;
                break;
            }
        }
        }
        else if(arr.length!=arr1.length){
            b=false;
        }
        
        return b;
        }
}
