class Solution {
    public String removeTrailingZeros(String num) {
        // int n=Integer.parseInt(num);
        // while(n%10==0){
        //     n=n/10;
        // }
        // return Integer.toString(n);
        int i=num.length()-1;
        while(num.charAt(i)=='0'){
            i--;
        }
        return num.substring(0,i+1);
    }
}
