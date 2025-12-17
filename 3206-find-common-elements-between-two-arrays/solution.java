class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        HashSet<Integer> setNums = new HashSet<>();
        for(int n : nums2) setNums.add(n);

        int c = 0;
        for(int n : nums1) {
            if(setNums.contains(n)) {
                c++;
            }
        }
        HashSet<Integer> setNums1 = new HashSet<>();
        for(int n : nums1) setNums1.add(n);

        int c1 = 0;
        for(int n : nums2) {
            if(setNums1.contains(n)) {
                c1++;
            }
        }
        return new int[]{c,c1};
    }
}
