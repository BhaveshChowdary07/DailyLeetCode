class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> combination = new ArrayList<>();
        getAllCombi(candidates, 0, target, answer, combination);
        return answer;
    }
    public static void getAllCombi(int[] candidates, int idx, int target,List<List<Integer>> answer, List<Integer> combination) {
        if (target == 0) {
            answer.add(new ArrayList<>(combination));
            return;
        }
        if (idx >= candidates.length || target < 0) {
            return;
        }
        combination.add(candidates[idx]);
        getAllCombi(candidates, idx, target - candidates[idx], answer, combination);
        combination.remove(combination.size() - 1);
        getAllCombi(candidates, idx + 1, target, answer, combination);
    }
}
