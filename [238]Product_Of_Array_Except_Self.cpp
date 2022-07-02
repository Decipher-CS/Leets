#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int postfix = 1;
        int prefix = 1;
        vector<int> result(nums.size(), 1) ;

        for (int res=0 , num=0; num < nums.size() ; ++num, ++res){
            result[res] *= prefix;
            prefix *= nums[num];
        }

        for (int res = nums.size()-1, num = nums.size()-1; num >= 0 ; --num, --res){
            result[res] *= postfix;
            postfix *= nums[num];
        }

        return result;
    }
};


int main(void){
    vector<int> nums = {1,2,3,4};
    Solution().productExceptSelf(nums);
    return 0;
}