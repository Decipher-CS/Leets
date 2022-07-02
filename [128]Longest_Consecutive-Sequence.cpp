#include<iostream>
#include<vector>
#include<map>
#include<unordered_map>
#include<algorithm>

using namespace std;


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result = 1;
        int diff = 1;
        if (!nums.size()) return 0;
        sort(begin(nums), end(nums));
        for (auto it : nums)
            cout << it << endl;

        for (auto num = nums.begin(); num != nums.end()-1; ++num){
            if ( (*(num+1)) == (*num) ) continue;
            if (   ( (*(num+1)) == ((*num)+1) )   ) {
                ++diff;
            } else {
                diff = 1;
            }
            if (diff > result){
                result = diff;
            }

        }
        return result;
    }

};


int main(){
    // vector<int> nums = {100,4,200,1,3,2}; // sol => 4
    // vector<int> nums = {0,3,7,2,5,8,4,6,0,1}; //sol => 8
    vector<int> nums = {1,2,0,1}; // sol => 3
    int sol = Solution().longestConsecutive(nums);
    cout << "\nSolution is : " << sol <<endl;
    return 0;
}