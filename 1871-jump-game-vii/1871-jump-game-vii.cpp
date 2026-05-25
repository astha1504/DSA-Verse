class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        vector<int> prefix(n+1, 0); // prefix sum of reachable counts
        vector<bool> reachable(n, false);
        
        reachable[0] = true;
        prefix[1] = 1; // prefix[1] counts reachable[0]
        
        for (int i = 1; i < n; i++) {
            if (s[i] == '0') {
                int left = max(0, i - maxJump);
                int right = i - minJump;
                if (right >= 0 && prefix[right+1] - prefix[left] > 0) {
                    reachable[i] = true;
                }
            }
            prefix[i+1] = prefix[i] + (reachable[i] ? 1 : 0);
        }
        
        return reachable[n-1];
    }
};
