import java.util.*;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            if (isOperator(token)) {
                int num2 = stack.pop();
                int num1 = stack.pop();
                stack.push(calculate(num1, num2, token));
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }

    public boolean isOperator(String token) {
        return token.equals("+") || 
               token.equals("-") || 
               token.equals("*") || 
               token.equals("/");
    }

    int calculate(int num1, int num2, String token) {
        switch (token) {
            case "+": return num1 + num2;
            case "-": return num1 - num2;
            case "*": return num1 * num2;
            case "/": return num1 / num2;
            default:
                throw new IllegalArgumentException("Invalid operator");
        }
    }
}
