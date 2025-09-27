class Solution {
    public String majorityFrequencyGroup(String s) {
        Map<Character,Integer> freMap=new HashMap<>();
        for(char c:s.toCharArray()){
            freMap.put(c,freMap.getOrDefault(c,0)+1);
        }
        Map<Integer,List<Character>> gmap=new HashMap<>();
        for(Map.Entry<Character,Integer> i:freMap.entrySet()){
            int freq=i.getValue();
            char ch=i.getKey();
            gmap.computeIfAbsent(freq,k -> new ArrayList<>()).add(ch);
        }
        int max=0;
        int maxfre=0;
        for(Map.Entry<Integer, List<Character>> e:gmap.entrySet()){
            int fre=e.getKey();
            List<Character> ch=e.getValue();
            int gps=ch.size();

            if(gps>max||(gps==max&&fre>maxfre)){
                max=gps;
                maxfre=fre;
            }
        }
    List<Character> majchars = gmap.get(maxfre);
    StringBuilder sb = new StringBuilder();
    for(char c:majchars){
        sb.append(c);
    }
return sb.toString();
    }
}
