class Solution {
    public boolean isPalindrome(String s) {
        //stack ? put in stack and pop it to see if it the same as every char
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int len = s.length();
        if(len == 0){
            return true; 
        }

        Stack<Character> stack = new Stack<>();
        for(char c : s.toCharArray()){
            stack.push(c);
        }

        for(int i=0; i<len;i++){
            if(stack.pop() != s.charAt(i)){
                return false; 
            }
        }

        return true;
    }
}