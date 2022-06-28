#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagramsV2(vector<string>& strs) {
        unordered_map<std::string, vector<string>> hm;
        vector<vector<string>> result;
        vector<string> temp_result;

        for (auto &str : strs)
                hm[sort_char(str)].push_back(str);

        for (auto &key : hm)
                result.push_back(key.second);

        return result;
    }

    string sort_char(string str){
        string temp_str = str;
        sort(begin(temp_str), end(temp_str));
        return temp_str;
    }


    vector<vector<string>> groupAnagramsV1(vector<string>& strs) {
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
    vector<vector<string>> sol = Solution().groupAnagramsV2(strs);
    for (auto strings : sol){
        for (auto str : strings){
            cout << str << " ";
        }
        cout << endl;
    }
    return 0;
}