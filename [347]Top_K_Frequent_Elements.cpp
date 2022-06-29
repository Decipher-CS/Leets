#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
            unordered_map<int, int> hm;
            vector<int> result;
            if (nums.size() == 1)
                return {nums};

            for (auto num : nums)
            {
                    ++hm[num];
            }
            for (int i = k; i > 0; --i)
            {
                double greatest_number[2] = {-999 , (-1 * numeric_limits<double>::infinity())};
                    for (auto key : hm)
                    {
                            // cout << key.first << " : " << key.second << endl;
                            if (greatest_number[1] <= key.second)
                            {
                                    greatest_number[0] = key.first;
                                    greatest_number[1] = key.second;
                            }
                    }
                    result.push_back(greatest_number[0]);
                    hm.erase(greatest_number[0]);
            }


            return result;
    }
};

int main(void){
    // vector<int> nums = {1,1,1,2,2,3};
    vector<int> nums = {3,0,1,0};
    // int k = 2;
    int k = 1;
    vector<int> solution = Solution().topKFrequent(nums, k);
    for (auto &it : solution)
        cout << it << endl;
    return 0;
}