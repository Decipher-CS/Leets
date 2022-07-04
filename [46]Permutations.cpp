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
    vector<vector<int>> permute0(vector<int>& nums){
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

    set<  pair< vector<int>, vector<vector<int>> >  > memo_set;
    vector<vector<int>>permute(vector<int>&nums){
        if (nums.size() == 1) return {nums};

            // Keep it here. Might need to refer it later on. //
        // const auto it = find_if( begin(memo_set), end(memo_set), []( const auto& p ){
            //  return p.first==nums; 
        // } );
        // const bool found = it != std::end(memo_set);
        vector<vector<int>> result;
        vector<vector<int>>temp_arr;
        int temp_val;


        auto found = memo_set.find(pair<vector<int>, vector<vector<int>>> (nums, result));

        if (found != memo_set.end()){
            return (*found).second;
        }
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

        memo_set.emplace(nums, result);

        return result;
    }
};

struct CustomCompare{
    bool operator() (const pair<vector<int>, vector<vector<int>>> &lhs, const pair<vector<int>, vector<vector<int>>> &rhs) const{
        return (lhs.first < rhs.first);
    }
};

int main(){
    vector<int> nums = {1,2,3,4,5,6};
    vector<vector<int>> solution = Solution().permute(nums);
    for (auto sol : solution){
        for (auto s : sol){
            cout << s << " ";
        }
        cout << endl;
    }

    // set<pair<vector<int>, vector<vector<int>>>, CustomCompare> memo_set;

    // memo_set.emplace(vector<int>{1,2,3}, vector<vector<int>>{{9181}});
    // memo_set.emplace(vector<int>{2,2,3}, vector<vector<int>>{{6,5,6}});
    // memo_set.emplace(vector<int>{3,2,3}, vector<vector<int>>{{7,5,6}});
    // memo_set.emplace(vector<int>{4,2,3}, vector<vector<int>>{{8,5,6}});

    // vector<vector<int>> n;

    // auto it = memo_set.find(pair<vector<int>,vector<vector<int>>> (nums, n));
    // if (it == end(memo_set)){
    //     cout << "\nnot found!\n";
    // } else{
    //     cout << "res ; " << (*it).second[0][0] << endl;
    // }

    // for (auto it : memo_set){
    //     for (auto itj : it.second){
    //         cout << it.first[0] << " : " << it << endl;
    //     }
    // }




    return 0;
}