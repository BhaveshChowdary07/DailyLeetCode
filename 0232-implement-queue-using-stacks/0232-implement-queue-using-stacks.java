import java.util.*;
class MyQueue {
    Stack<Integer> stack;
    public MyQueue() {
        stack = new Stack<>();
    }
    public void push(int x) {
        stack.push(x);
    }
    
    public int pop() {
        int removed = 0;
        if(!stack.isEmpty()){
            Collections.reverse(stack);
            removed = stack.pop();
            Collections.reverse(stack);
        }
        return removed;
    }
    
    public int peek() {
        int peek = -1;
        if(!stack.isEmpty()){
        Collections.reverse(stack);
        peek = stack.peek();
        Collections.reverse(stack);
        return peek;}
        return peek;
    }
    
    public boolean empty() {
        return stack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */