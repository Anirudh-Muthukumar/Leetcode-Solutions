/*
    Time complexity : O(n)
    Space complexitY: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n==0)
            return 0;
        int min_buy = prices[0];
        int max_sell = 0;
        for(int i = 0; i < n; ++i){
            min_buy = min(min_buy, prices[i]);
            max_sell = max(max_sell, prices[i] - min_buy);
        }
        
        return max_sell;
        
//         int K = 1;
//         vector<vector<int>> dp(K + 1, vector<int>(n, 0));
//         for(int k = 1; k <= K; ++k){
//             int buy = prices[0];
//             for(int i = 1; i < n; ++i){
//                 buy = min(buy, prices[i] - dp[k-1][i-1]);
//                 dp[k][i] = max(dp[k][i-1], prices[i] - buy);
//             }
//         }
        
//         return dp[K][n-1];
    }
};