#include <bits/stdc++.h>
using namespace std;

long long Reduction(vector<int>& Array, int N, int H, int K){
    long long Sum = 0;
    for(int i = 0; i < N; i++){
        if(Array[i] <= H){
            continue;
        }else{
            Sum += abs(Array[i] - H);
        }
    }
    return Sum;
}

int BinarySearch(vector<int>& Array, int N, int K){
    int low = 0;
    int high = 1000000;
    int ans;

    while(low <= high){
        long long mid = low + (high - low)/2;
        long long Sum = Reduction(Array, N, mid, K);

        if(Sum < K){
            ans = mid;
            high = mid-1;
        }
        else if(Sum >= K){
            low = mid+1;
        }
    }
    return ans-1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while(T--){
        int N, K;
        cin >> N >> K;

        vector<int> Array(N);
        for(int i = 0; i < N; i++){
            cin >> Array[i];
        }

        // sort(Array.begin(), Array.end());
        cout << BinarySearch(Array, N, K) << "\n";
    }   
    return 0;
}