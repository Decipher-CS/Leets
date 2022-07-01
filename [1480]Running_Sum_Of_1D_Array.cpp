#include<iostream>
#include<vector>
#include<map>
#include<unordered_map>

using namespace std;

// TODO //
// Try Recursion //

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < nums.size() ; ++i){
            // cout << nums[i] << endl;
            if (i==0){
                result.push_back(0 + nums[i]);
            } else
                result.push_back(result[i-1] + nums[i]);
        }
        for (auto res : result)
            cout << res << endl;

        return result;
    }
};


int main(){
    vector<int> nums = {1,2,3,4};
    Solution().runningSum(nums);
    return 0;
}