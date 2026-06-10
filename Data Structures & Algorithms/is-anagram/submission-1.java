class Solution {
    public boolean isAnagram(String s, String t) {
        //edge case: s.length != t.length
        //normal: loop-through s, and t check each char occurence. (encode method is the key)
        int slen = s.length();
        int tlen = t.length();

        if(slen != tlen){
            return false; 
        }

        int[] count = new int[26]; //use hashTable 

        for(int i=0; i<slen; i++){
            count[s.charAt(i)-'a']++;
            count[t.charAt(i)-'a']--;
        }

        for(int val : count){
            if(val != 0){
                return false;
            }
        }

        return true;
    }
}
