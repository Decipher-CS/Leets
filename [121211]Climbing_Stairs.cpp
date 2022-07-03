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
    int climbStairs(int n) {
        vector<int> ones(n, 1);
        int steps = 0;

        auto limiter = (n % 2 == 0) ? ones.size()/2 : int(ones.size()/2) ;

        for (int i = 0; i < limiter; i++){
            ones[i] = 2;
            // ones.erase(ones.begin() + i + 1);
            ones.pop_back();
            if (i==limiter-1){
                steps ++;
            } else
                steps += ones.size();
        }
        return steps+1;
    }

};


int main(){
    vector<int> n = {1,2,3,4,5,6};
    vector<int> solutions;
    for (auto n : n){
        solutions.push_back( Solution().climbStairs(n) );
    }
    cout << "\nSolutions are :" << endl;
    for (int i=0; i<n.size(); ++i)
        cout << n[i] << " => "<< solutions[i] << " steps" << endl;

    return 0;
}