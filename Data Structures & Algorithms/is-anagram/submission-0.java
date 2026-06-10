class Solution {
    public boolean isAnagram(String s, String t) {
        //edge case: s.length != t.length
        //normal: loop-through s, and t check each char occurence. (encode method is the key)
        int slen = s.length();
        int tlen = t.length();

        if(slen != tlen){
            return false; 
        }

        Map<Character,Integer> map = new HashMap<>();
        for(int i=0;i<slen;i++){
            char cur = s.charAt(i);
            if(map.containsKey(cur)){
                map.put(cur,map.get(cur)+1); //getOrDefault(cur,1)
            }else{
                map.put(cur,1);
            }
        }

        for(int i=0;i<tlen;i++){
            char cur = t.charAt(i);
            if(map.containsKey(cur)){
                map.put(cur,map.get(cur)-1);
            }else{
                map.put(cur, -1);
            }
        }

        for(char key: map.keySet()){
            if(map.get(key)!=0){
                return false;
            }
        }

        return true;
    }
}
