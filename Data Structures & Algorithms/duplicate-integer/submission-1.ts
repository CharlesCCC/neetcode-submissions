class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const check = new Set<number>
        for(const num of nums){
            if(check.has(num)){
                return true; 
            }
            check.add(num);
        }

        return false;
    }
}
