#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result = {};
        vector<string> temp_res;

        for (auto it = begin(strs); it!=end(strs); ++it){
            temp_res.push_back(*it);
            for (auto itj = begin(strs); itj != end(strs); ++itj){
                if (*it == *itj){
                    continue;
                } 
                if (isAnagram((*it) , *itj)){
                    temp_res.push_back(*itj);
                    strs.erase(itj);
                }
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
        
        for (int i = 0; i< str1.length(); i++){
            int f;
            if (  (f = str2.find(str1[i]))  == -1  )
                return false;
            str2.erase(f,f);
        }
        return true;
    }
};

int main(void){
    vector<string> strs = {"eat","tea","tan","ate","nat","bat"};
    vector<vector<string>> result = {{"bat"},{"nat","tan"},{"ate","eat","tea"}};
    vector<vector<string>> sol = Solution().groupAnagrams(strs);
    for (auto strings : sol){
        for (auto str : strings){
            cout << str << " ";
        }
        cout << endl;
    }
    // string s = "hello";
    // cout << typeid(s).name() << endl;
    // for (auto it = begin(strs);  it != end(strs); ++it){
    //     cout << typeid(string(*it)).name() << endl;
    // }

    // cout << endl;
    // cout << endl;
    // cout << endl;

    // for (auto str : strs){
    //     cout << typeid(str).name() << endl;
    // }

    return 0;
}