class Solution {
    public String fractionToDecimal(int num, int din) {
        if(num == 0)return "0";
        StringBuilder sb = new StringBuilder();
        if (num < 0 ^ din<0) sb.append("-");
        long n = Math.abs((long)num);
        long d = Math.abs((long)din);
        sb.append(n/d);
        if(n%d == 0) return sb.toString();
        sb.append(".");
        Map<Long,Integer> seen = new HashMap<>();
        for(long r = n%d; r>0; r%=d){
            if(seen.containsKey(r)){
                sb.insert(seen.get(r),"(");
                sb.append(")");
                break;
            }
            seen.put(r,sb.length());
            r*=10;
            sb.append(r/d);
        }
        return sb.toString();
    }
}