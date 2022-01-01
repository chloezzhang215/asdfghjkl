class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);
        
        int current = 0;
      
        for (int num : arr) {
        current = Math.min(current + 1, num);
        }
    return current;
    }
}
