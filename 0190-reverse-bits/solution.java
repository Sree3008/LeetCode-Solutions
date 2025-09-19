class Solution {
    public int reverseBits(int n) {
        String str = String.format("%32s", Integer.toBinaryString(n)).replace(' ', '0');
        StringBuilder sb=new StringBuilder(str);
        String s=sb.reverse().toString();
        int res=(int) Long.parseLong(s,2);
        return res;
    }
}
