class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        //use a map to keep track of the needed value and its index 
        const res:number[] = []
        const map = new Map<number,number>()

        for(let i=0; i < nums.length; i++){
            const curN = nums[i]
            const need = target - curN
            if(map.has(need)){
                res[0]=map.get(need) as number
                res[1]=i;

                return res;
            }
            map.set(curN,i)
        }

        return res; 
    }
}
