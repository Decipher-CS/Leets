#include<iostream>
#include<vector>
#include<map>
#include<unordered_map>
#include<algorithm>
#include<set>
#include<unordered_set>

using namespace std;


class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums){
        if (nums.size() == 1) return {nums};
        vector<vector<int>> result;
        vector<vector<int>>temp_arr;
        int temp_val;

        for (int i=0; i<nums.size(); ++i){
            temp_val = nums[i];
            nums.erase(begin(nums) + i);
            temp_arr = permute(nums);
            for (auto val : temp_arr){
                val.push_back(temp_val);
                result.push_back(val);
            }
            nums.insert(begin(nums)+i, temp_val);
            temp_arr.clear();
        }
        return result;
    }

};


int main(){
    vector<int> nums = {1,2,3};
    vector<vector<int>> solution = Solution().permute(nums);
    for (auto sol : solution){
        for (auto s : sol){
            cout << s << " ";
        }
        cout << endl;
    }
    return 0;
}