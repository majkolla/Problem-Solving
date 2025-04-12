#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> v(n);
    // Frequencies for vertices 1..n+1 (we use size n+2 for safe indexing)
    vector<int> freq(n + 2, 0);

    // Read the 'v' column and check range
    for(int i = 0; i < n; i++){
        cin >> v[i];
        if(v[i] < 1 || v[i] > n + 1){
            cout << "Error\n";
            return 0;
        }
        freq[v[i]]++;
    }

    // A min-structure of leaves (vertices with freq == 0)
    set<int> leaves;
    for(int x = 1; x <= n + 1; x++){
        if(freq[x] == 0){
            leaves.insert(x);
        }
    }

    vector<int> ucol(n); // to store the reconstructed u-column

    // Simulate the leaf-picking process
    for(int i = 0; i < n; i++){
        if(leaves.empty()){
            // no leaf available => inconsistent
            cout << "Error\n";
            return 0;
        }
        // pick the smallest leaf
        int u = *leaves.begin();
        leaves.erase(leaves.begin());
        ucol[i] = u;

        // decrement freq of v[i]
        int w = v[i];
        freq[w]--;
        if(freq[w] < 0){
            // invalid, used w too many times
            cout << "Error\n";
            return 0;
        }
        // if w is now a leaf, add it
        if(freq[w] == 0){
            leaves.insert(w);
        }
    }

    // after n removals, exactly one vertex should remain
    if(leaves.size() != 1){
        cout << "Error\n";
        return 0;
    }

    // output the reconstructed u-column
    for(int i = 0; i < n; i++){
        cout << ucol[i] << "\n";
    }
    return 0;
}
