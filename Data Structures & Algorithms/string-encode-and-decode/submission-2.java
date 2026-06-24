class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s : strs){
            sb.append(s.length()).append('#').append(s);
        }

        return sb.toString();
    }

    //e.g. 3#abc4#abcd
    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0; 
        while(i<str.length()){
            int j = i;
            //find length 
            while(str.charAt(j) != '#'){
                j++; 
            }
            int length = Integer.parseInt(str.substring(i,j));
            i = j+1; //skip # 
            j = i + length; // grab next size 

            res.add(str.substring(i,j));
            i = j; 
        }

        return res; 
    }
}
