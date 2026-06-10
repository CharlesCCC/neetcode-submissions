class Solution {
    public int[] twoSum(int[] nums, int target) {
        //1, find the 1st element X[j]  
        //2, loop through remaining to see if target - nums[i] = X
        //3, repeat until target - nums[i] = X and return 

        int len = nums.length;
        int[] res = new int[2];

        if(len <= 1){
            return res;
        }

        //key: num, value: index
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0; i<len; i++){
            int cur = nums[i];
            int need = target - cur; 
            //we have find the need
            if(map.containsKey(need)){
                res[0] = map.get(need);
                res[1] = i;

                return res;
            }else{
                map.put(cur, i);
            }
        }
        return res;
    }
}
