#include <iostream>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1)
            return s;

        string result[numRows];
        string final_str = "";
        int inc = 0;
        int inc_amount = 1;

        for (int i = 0; i < s.length(); ++i){
            result[inc] += s[i];
            if ((inc == 0) and (inc_amount == -1)){
                inc_amount *= -1;
            } else if ((inc == numRows-1) && (inc_amount == 1)){
                inc_amount *= -1;
            }
            inc += inc_amount;
        }

        for (int i=0; i<numRows; i++){
            for (int j=0; j< result[i].length() ; j++)
                final_str += result[i][j];
        }

        return final_str;
    }
};

int main(void){
    int rows = 3;
    string inputs[rows][3] = {
        {"ABCD", "2", "ACBD"},
        {"PAYPALISHIRING", "3","PAHNAPLSIIGYIR"},
        {"ABCDE", "3" ,"AEBDC"}
    };

    for (int i=0; i<rows; i++){
        if ( inputs[i][2] == Solution().convert(inputs[i][0], stoi(inputs[i][1])) ){
            cout << "Correct" << endl;
        } else
            cout << "Incorrect Answer" << endl;
        cout << endl;
    }
    return 0;
}