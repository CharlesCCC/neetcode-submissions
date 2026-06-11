class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        //fill the set
        for(int num : nums){
            numSet.add(num);
        }

        int longest = 0;

        //loop through the nums 
        for(int num : nums){
            if(!numSet.contains(num-1)){ //check num-1 not in the set
            //This guarantees that each consecutive sequence is counted exactly once.
                int length = 1;
                while(numSet.contains(num + length)){
                    length++;
                }
                longest = Math.max(longest,length);
            }
        }
        return longest; 
    }
}
