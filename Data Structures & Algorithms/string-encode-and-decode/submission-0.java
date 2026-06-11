class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s : strs){
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while(i < str.length()){
            int j = i; //move j up to where i started 

            while(str.charAt(j) != '#'){  //not at the # mark yet
                j++; 
            }
            int length = Integer.parseInt(str.substring(i,j));
            i = j + 1; //move to next char after length 
            j = i + length; //skip next length chars 

            res.add(str.substring(i,j)); //grab next string
            i = j; //reset i = j (new starting point)
        }

        return res; 
    }
}
