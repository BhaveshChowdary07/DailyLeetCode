class Solution {
    public boolean checkValidString(String s) {
        int cmin = 0; // Minimum possible open parentheses
        int cmax = 0; // Maximum possible open parentheses

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                cmin++;
                cmax++;
            } else if (ch == ')') {
                cmin--;
                cmax--;
            } else if (ch == '*') {
                // '*' can be '(', ')' or empty, so adjust bounds
                cmin--;    // assume '*' as ')'
                cmax++;    // assume '*' as '('
            }

            // If cmax goes negative, too many ')' have been encountered
            if (cmax < 0) {
                return false;
            }

            // Ensure cmin is never negative (we can't have less than 0 open)
            cmin = Math.max(cmin, 0);
        }

        // If we can balance all open brackets, return true
        return cmin == 0;
    }
}
