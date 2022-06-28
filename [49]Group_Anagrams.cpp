#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result = {};
        vector<string> temp_res;
        while (strs.size() > 0)
        {
            string current_elem = strs.at(strs.size()-1);
            temp_res.push_back(current_elem);
            strs.pop_back();
            for (int i = 0; i < strs.size(); i=i)
            {
                if (isAnagram(current_elem, strs[i]))
                {
                    temp_res.push_back(strs[i]);
                    strs.erase(strs.begin()+i);
                } else
                    ++i;
            }
            result.push_back(temp_res);
            temp_res.clear();
        }


        return result;
    }

public:
    bool isAnagram(string str1, string str2) {
        if (str1.length() != str2.length())
            return false;
        
        int f;
        for (int i = 0; i< str1.length(); i++){
            if (  (f = str2.find(str1[i]))  == -1  )
                return false;
            str2.erase(str2.begin()+f);
        }
        return true;
    }
};

int main(void){
    vector<string> strs = {"eat","tea","tan","ate","nat","bat"};
    // vector<string> strs = {"a","a","a"};
    // vector<string> strs = {"abbbbbbbbbbb","aaaaaaaaaaab"};
    vector<vector<string>> sol = Solution().groupAnagrams(strs);
    for (auto strings : sol){
        for (auto str : strings){
            cout << str << " ";
        }
        cout << endl;
    }
    // string str1 = strs[0];
    // string str2 = strs[3];
    // cout << Solution().isAnagram(str2, str1) << endl;
    return 0;
}