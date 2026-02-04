import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class LockingTree {
    private int[] parent;
    private List<Integer>[] childs;
    private int[] locker;
    private int[] ctofLocks;
    
    public LockingTree(int[] parent) {
        this.parent = parent;
        int n = parent.length;
        childs = new ArrayList[n];
        locker = new int [n];
        ctofLocks = new int [n];
        Arrays.fill(locker,-1);
        for(int i = 0 ; i<n;i++){
            childs[i] = new ArrayList<>();
        }
        for(int i = 1; i<n;i++){
            childs[parent[i]].add(i);
        }
    }
    
    public boolean lock(int num, int user) {
        if (locker[num] != -1) return false;
        locker[num] = user;
        inform(num,+1);
        return true;
    }
    
    public boolean unlock(int num, int user) {
        if (locker[num] != user) return false;
        locker[num] = -1;
        inform(num,-1);
        return true;
    }
    
    public boolean upgrade(int num, int user) {
        if (locker[num] != -1 || ctofLocks[num] == 0)return false;
        int p = parent[num];
        while (p != -1){
            if(locker[p]!=-1) return false;
            p = parent[p];
        }
        int count = ctofLocks[num];
        releaseLocks(num);
        inform(num,-count);
        locker[num] = user;
        inform(num,+1);
        return true;
    }
    private void inform(int num,int ct){
        int p = parent[num];
        while (p != -1){
            ctofLocks[p] += ct;
            p = parent[p];
        }
    }
    private void releaseLocks(int num){
        locker[num] = -1;
        ctofLocks[num] = 0;
        for(int child : childs[num])
            if(locker[child] != -1 || ctofLocks[child] > 0)
                releaseLocks(child);
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = new LockingTree(parent);
 * boolean param_1 = obj.lock(num,user);
 * boolean param_2 = obj.unlock(num,user);
 * boolean param_3 = obj.upgrade(num,user);
 */