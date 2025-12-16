class Solution {
    public int minimizedStringLength(String s) {
        char[] ch=s.toCharArray();
        Set<Character> list=new HashSet<>();
        for(char i:ch){
            list.add(i);
        }
        return list.size();
    }
}
