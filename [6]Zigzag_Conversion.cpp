#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        
};

int main(void){
    string str = "PAYPALISHIRING";
    string ans = "PAHNAPLSIIGYIR";
    int numRows = 3;

    if (Solution().convert(str, numRows)  != ans){
        cout << "\n\nWrong answer\n\n" << endl;
    } else cout << "\n\nCORRECT!\n\n" << endl;
    
    return 0;
}