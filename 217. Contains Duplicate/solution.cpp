/*
Time complexity : O(n log n) 
Space complexity: O(1)

*/

#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        sort(begin(nums), end(nums));
        for(int i = 1; i < n; ++i)
            if(nums[i] == nums[i-1])
                return true;
        return false;
    }
};