#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<set>
#include<unordered_set>
#include <unordered_map>
using namespace std;


class Solution {
public:
    map< vector<int>, vector<vector<int>> > memo;
    vector<vector<int>> permute(vector<int>& nums){
        if (nums.size() == 1) return {nums};
        vector<vector<int>> result;
        vector<vector<int>>temp_arr;
        int temp_val;

        for (int i=0; i<nums.size(); ++i){
            temp_val = nums[0];
            nums.erase(begin(nums));
            temp_arr = permute(nums);
            for (auto arr : temp_arr){
                arr.push_back(temp_val);
                result.push_back(arr);
            }
            nums.push_back(temp_val);
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