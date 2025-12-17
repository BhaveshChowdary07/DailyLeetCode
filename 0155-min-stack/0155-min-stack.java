// 2 stacks 

// import java.util.*;
// class MinStack {
//     private Stack<Integer> stack;
//     private Stack<Integer> minstack;
//     public MinStack() {
//         stack = new Stack<>();
//         minstack = new Stack<>();
//     }
    
//     public void push(int val) {
//         stack.push(val);
//         if(minstack.isEmpty()||val<=minstack.peek()){
//             minstack.push(val);
//         }
//     }
    
//     public void pop() {
//         int removed = stack.pop();
//         if(removed == minstack.peek()){
//             minstack.pop();
//         }
//     }
    
//     public int top() {
//         return stack.peek();
//     }
    
//     public int getMin() {
//         return minstack.peek();
//     }
// }

//single stack 

class MinStack {
    private Stack<int[]> minstack;
    public MinStack() {
        minstack = new Stack();
    }

    public void push(int val) {
       int min = minstack.isEmpty() ? val : Math.min(val, minstack.peek()[1]);
       minstack.push(new int[] {val , min}); 
    }
    
    public void pop() {
        minstack.pop();
    }
    
    public int top() {
        return minstack.peek()[0];
    }
    
    public int getMin() {
        return minstack.peek()[1];
    }
}


/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */