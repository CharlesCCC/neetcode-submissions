class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if(s.length !== t.length){
            return false; 
        }

        const cs = {};
        const ct = {}; 

        for(let i = 0; i < s.length; i++){
            cs[s[i]] = (cs[s[i]] || 0) + 1;
            ct[t[i]] = (ct[t[i]] || 0) + 1;
        }

        for(const key in cs){
            if(cs[key] !== ct[key]){
                return false; 
            }
        }

        return true; 
    }
}
