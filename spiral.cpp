#include <bits/stdc++.h>
using namespace std;

void SpiralPattern(int N) {
    vector<vector<char>> matrix(N, vector<char>(N, ' '));

    int top = 0, bottom = N-1;
    int left = 0, right = N-1;
    int count = 0;
    
    while((top <= bottom) && (left <= right)){
        for(int j = left; j <= right; j++){
            matrix[top][j] =  '*'; 
            if(count == 1) {
                left++;
                count = 0;
            }
        }
        top++;
        count = 1;
        
        for(int i = top; i <= bottom; i++){
            matrix[i][right] = '*';
            if(count == 1) {
                top++;
                count = 0;
            }     
        }
        right--;
        count = 1;

        if(top <= bottom){
            for(int j = right; j >= left; j--){
                matrix[bottom][j] = '*';
                if(count == 1) {
                    right--;;
                    count = 0;
                } 
                 
            }
            bottom--;
            count = 1;
        }

        if(left <= right) {
            for(int i = bottom; i >= top; i--){
                matrix[i][left] = '*';
                if(count == 1) {
                    bottom--;;
                    count = 0;
                }
            }
            left++;
            count = 1;
        }
    }

    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++){
            if(j < (N-1)) {
                if(matrix[i][j] == '*') cout << "* ";
                else cout << "  ";
            }
            else{
                cout << matrix[i][j];
            }
        }
        cout << "\n";
    }
    
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 0;
    cin >> T;

    for(int L = 1; L <= T; L++) {
        int N;
        cin >> N;
        
        cout << ("Case #" + to_string(L) + ":\n");
        SpiralPattern(N);
    }

    return 0;
}