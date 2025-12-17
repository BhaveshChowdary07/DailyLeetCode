class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<s.length();i++){
            if(stack.size() != 0 && s.charAt(i)==stack.peek()){
                stack.pop();
            }
            else{
                stack.push(s.charAt(i));
            }
        }
        StringBuilder res=new StringBuilder(); 
        for(char ch:stack ){
            res.append(ch);
        }
        return res.toString();
    }
}