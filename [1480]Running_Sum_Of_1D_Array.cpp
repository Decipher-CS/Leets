#include<iostream>
#include<vector>
#include<map>
#include<unordered_map>

using namespace std;

// TODO //
// Try Recursion //

class Solution {
public:
    // ITERATIVE SOLUTION
    vector<int> result;
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
    // RECURSIVE SOLUTION
    vector<int> runningSum_recursion(vector<int>& nums) {
        if (nums.size() == 1)   return nums;
        int temp_val = nums[nums.size()-1];
        nums.pop_back();
        nums = Solution().runningSum_recursion(nums);
        nums.push_back(temp_val + nums[nums.size()-1]);
        return nums;
    }

};


int main(){
    vector<int> nums = {1,2,3,4};
    vector<int> result = Solution().runningSum_recursion(nums);
    for (auto res :result )
        cout << res << endl;
    return 0;
}