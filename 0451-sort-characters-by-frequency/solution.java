class Solution {
    public String frequencySort(String s) {
        char[] arr=s.toCharArray();
        HashMap<Character,Integer> list=new HashMap<>();
        Arrays.sort(arr);
        for(int i=0;i<arr.length;i++){
             if (list.containsKey(arr[i])) continue;
            int c=0;
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]==arr[j]){
                    c++;
                }
            }
            
                list.put(arr[i],c+1);
        }
        List<Map.Entry<Character, Integer>> sortedList = new ArrayList<>(list.entrySet());
        sortedList.sort((a, b) -> b.getValue() - a.getValue());

        StringBuilder sb = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : sortedList) {
            for (int k = 0; k < entry.getValue(); k++) {
                sb.append(entry.getKey());
            }
        }
        return sb.toString();

    }
}
