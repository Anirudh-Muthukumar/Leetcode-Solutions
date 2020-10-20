/*
Idea: Kadane's algorithm

    Time complexity: O(n)
    Space complexity: O(1)
*/

#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int max_so_far = INT_MIN;
        int curr_sum = 0;
        for(int i = 0; i < n; ++i){
            curr_sum += nums[i];
            max_so_far = max(max_so_far, curr_sum);
            if(curr_sum < 0)
                curr_sum = 0;
        }
        return max_so_far;
    }
};