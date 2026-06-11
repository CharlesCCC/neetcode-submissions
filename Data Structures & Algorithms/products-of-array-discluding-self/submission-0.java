class Solution {
    public int[] productExceptSelf(int[] nums) {
        //prefix/suffix sum
        int n = nums.length;
        int[] pref = new int[n];
        int[] suff = new int[n];
        int[] res = new int[n];

        //initial boundry value 
        pref[0] = 1;
        suff[n-1] = 1;

        //compute prefix (from left to right)
        for(int i=1;i<n;i++){
            pref[i] = nums[i-1] * pref[i-1];
        }

        //compute suffix (from right to left)
        for(int i=n-2; i>=0; i--){
            suff[i] = nums[i+1] * suff[i+1];
        }

        //compute final ressults
        for(int i=0; i<n;i++){
            res[i]=pref[i] * suff[i];
        }

        return res;

    }
}  
