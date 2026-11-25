class Solution {
    public int longestConsecutive(int[] nums) {
        int lenghtList = 1;
        int maxLenght = 1;

        Arrays.sort(nums);

        if(nums.length == 0){
            return 0;
        }

        for (int i = 0; i < nums.length -1; i++) {
            if (nums[i] == nums[i + 1]) {
                continue;
            }

            if (nums[i] + 1 == nums[i + 1]) {
                lenghtList++;
            } else {
                if (maxLenght < lenghtList) {
                    maxLenght = lenghtList;
                }
                lenghtList = 1;
            }
        }

        return Math.max(maxLenght, lenghtList);
    }
}
