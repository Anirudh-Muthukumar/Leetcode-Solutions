#include<map>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res(2, -1);
        map<int, int> hash;
        for(int i = 0; i < n; ++i){
            if(hash.find(k - nums[i]) != hash.end()){
                res = {hash[k - nums[i]], i};
                return res;
            }
            hash[nums[i]] = i;
        }
        return res;
    }
};