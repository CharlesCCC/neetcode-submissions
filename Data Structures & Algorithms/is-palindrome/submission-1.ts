class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        let newStr = ''
        for (let c of s){
            if(this.alphaNum(c)){
                newStr += c.toLocaleLowerCase();
            }
        }

        return newStr === newStr.split('').reverse().join('');
    }

    alphaNum(c){
        return (
            (c >= 'A' && c <= 'Z') || 
            (c >= 'a' && c <= 'z') ||
            (c >= '0' && c <= '9')
        );
    }
}
