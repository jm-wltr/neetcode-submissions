class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;

        int[] difference = new int[n];
        for (int j = 0; j < n; j++) {
            difference[j] = target - nums[j];
        }

        Map<Integer, Integer> differenceIndex = new HashMap<>();
        for (int i = 0; i < n; i++) {
            differenceIndex.put(difference[i], i);
        }
        Integer j;
        for (int i = 0; i < n; i++) {
            j = differenceIndex.get(nums[i]);
            if (j != null && j > i) {
                int[] result = new int[2];
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
        return null;
    }
}





