class Solution {
    public boolean hasDuplicate(int[] nums) {
        //edge cases: if nums <= 1 (false)
        //normal: loop through all and check within set 
        int len = nums.length;
        Set<Integer> check = new HashSet<>();

        if(len <= 1){
            return false; 
        }

        for(int i=0; i<len;i++){
            if(!check.add(nums[i])){
                return true;
            }
        }

        return false;
    }
}