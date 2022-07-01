#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        unordered_map<int, int> prefix_storage; 
        unordered_map<int, int> postfix_storage;
        vector<int> sample_array;

        int arr_last = nums.size()-1;
        prefix_storage[0] = nums[0];
        postfix_storage[arr_last] = nums[arr_last];

        for (int i=1; i < nums.size() ; ++i)   prefix_storage[i] = nums[i] * prefix_storage[i-1];
        for (int i=arr_last-1; i >= 0 ; --i)   postfix_storage[i] = nums[i] * postfix_storage[i+1];

        for (int i=1; i<arr_last; ++i)   nums[i] = prefix_storage[i-1] * postfix_storage[i+1];

        nums[0] = postfix_storage[1];
        nums[arr_last] = prefix_storage[arr_last-1];

        return nums;
    }
};


int main(void){
    vector<int> nums = {1,2,3,4};
    Solution().productExceptSelf(nums);
    return 0;
}