class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //encode each string as int[26] array --> key 
        //edge case: strs empty or just one 
        int len = strs.length;

        //key: int[26] to string,  value: str[i]
        Map<String,List<String>> map = new HashMap<>();
        for(String s : strs){
            int[] encode = new int[26];
            for(char c : s.toCharArray()){
                encode[c-'a']++;
            }
            //encode to String ? 
            String encoded = Arrays.toString(encode);
            map.putIfAbsent(encoded,new ArrayList<>());
            map.get(encoded).add(s);
            // Map.put(encoded, map.getOrDefault(encoded,new ArrayList<String>()).add(s));
        }

        //covert map of List<String> into two dimension array ?
        return new ArrayList<>(map.values());

    }
}
