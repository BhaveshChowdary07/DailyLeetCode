class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int gassum = 0;
        int costsum = 0;
        for(int g : gas){
            gassum = gassum+g;
        }
        for(int c : cost){
            costsum = costsum+c;
        }
        if (gassum<costsum)return -1;
        int start = 0;
        int rem = 0;
        for(int i = 0;i<=cost.length-1;i++){
            rem += gas[i] - cost[i];
            if(rem<0){
                start = i+1;
                rem = 0;
            }
            
        }
        return start;
    }
}