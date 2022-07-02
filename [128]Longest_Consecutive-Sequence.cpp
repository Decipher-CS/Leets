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
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int seq_size;
        int result = 0;


        for (auto num : nums_set){
            seq_size = 0;
            if (nums_set.find(num-1) != end(nums_set)) continue;
            while (nums_set.find(num+seq_size) != end(nums_set)) { seq_size++; }
            result = (seq_size > result) ? seq_size : result ;
        }
        
        return result;
    }
};


int main(){
    vector<int> nums = {100,4,200,1,3,2}; // sol => 4
    // vector<int> nums = {0,3,7,2,5,8,4,6,0,1}; //sol => 8
    // vector<int> nums = {1,2,0,1}; // sol => 3
    int sol = Solution().longestConsecutive(nums);
    cout << "\nSolution is : " << sol <<endl;


    return 0;
}