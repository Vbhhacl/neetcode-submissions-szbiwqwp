#include <string>
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        // Convert vector to a hash set for O(1) lookups
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());
        
        int n = s.length();
        // dp[i] means s[0...i-1] can be segmented into dictionary words
        std::vector<bool> dp(n + 1, false);
        
        // Base case: empty string is always valid
        dp[0] = true;
        
        // Iterate through all lengths of the string
        for (int i = 1; i <= n; i++) {
            // Check all possible partitions from 0 to i-1
            for (int j = 0; j < i; j++) {
                // If s[0...j-1] is valid and s[j...i-1] is a valid word
                if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break; // No need to check other partitions for this i
                }
            }
        }
        
        return dp[n];
    }
};