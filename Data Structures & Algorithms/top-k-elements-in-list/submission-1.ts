class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        //PQ - min.Heap (from small to big)
        //build the map
        const count = {};
        for(const num of nums){
            count[num] = (count[num] || 0 ) + 1
        }

        //create the min.heap 
        const heap = new MinPriorityQueue((x) => x[1]); //order by 2nd elemnt value 
        for(const [num, cnt] of Object.entries(count)){
            heap.enqueue([num,cnt]);
            if(heap.size() > k){
                heap.dequeue();
            }
        }

        //put into results 
        const res = [];
        for(let i=0; i < k; i++){
            const [num,cnt] = heap.dequeue();
            res.push(num)
        }

        return res; 
    }
}
