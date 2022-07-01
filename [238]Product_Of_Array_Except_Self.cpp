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



                    // TESTING PREFIX //
        for (int i=0; i < nums.size() ; ++i){
            if (i == 0){
                sample_array.push_back(nums[i]);
            } else
                sample_array.push_back(  nums[i] * sample_array[i-1]  );
        }

        for (auto num : sample_array)
            cout << num << endl;

        return {1,2,3};
    }
};


int main(void){
    vector<int> nums = {1,2,3,4};
    Solution().productExceptSelf(nums);
    return 0;
}