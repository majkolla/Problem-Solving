#include <bits/stdc++.h>

using namespace std;

struct DoubleHash {
    unsigned long long h1;
    unsigned long long h2;

    bool operator==(const DoubleHash &o) const {
        return (h1 == o.h1 && h2 == o.h2);
    }
};

struct DoubleHashHasher {
    size_t operator()(const DoubleHash &dh) const {
        auto h1 = dh.h1;
        auto h2 = dh.h2;
        const auto magic = 0x9e3779b97f4a7c15ULL;
        size_t res = (size_t)h1;
        res ^= (size_t)h2 + magic + (res << 6) + (res >> 2);
        return res;
    }
};


static const unsigned long long base1 = 131542391ULL; 
static const unsigned long long base2 = 2654435789ULL; 
struct RollingHash {
    vector<unsigned long long> prefix1, prefix2;
    vector<unsigned long long> power1, power2;
    int n;

    RollingHash(const string &s) {
        n = (int)s.size();
        prefix1.resize(n+1, 0ULL);
        prefix2.resize(n+1, 0ULL);
        power1.resize(n+1, 1ULL);
        power2.resize(n+1, 1ULL);

        for(int i = 1; i <= n; i++){
            power1[i] = power1[i-1] * base1;
            power2[i] = power2[i-1] * base2;
        }

        for(int i = 0; i < n; i++){
            prefix1[i+1] = prefix1[i] * base1 + (unsigned char)s[i];
            prefix2[i+1] = prefix2[i] * base2 + (unsigned char)s[i];
        }
    }

    DoubleHash getHash(int pos, int length) const {
        unsigned long long h1 = prefix1[pos+length] - prefix1[pos] * power1[length];
        unsigned long long h2 = prefix2[pos+length] - prefix2[pos] * power2[length];
        return DoubleHash{h1, h2};
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(true){
        int n;
        cin >> n;
        if(!cin || n == 0){
            break;
        }
        vector<string> seq(n);
        for(int i=0; i<n; i++){
            cin >> seq[i];
        }

        int needed = (n/2) + 1;

        vector<RollingHash> rh;
        rh.reserve(n);
        int minLen = INT_MAX;
        for (int i=0; i<n; i++){
            rh.emplace_back(seq[i]);
            minLen = min(minLen, (int)seq[i].size());
        }

        int low = 1, high = minLen;
        int bestLen = 0;
        vector<DoubleHash> bestHashes;

        while(low <= high){
            int mid = (low + high) / 2;

            unordered_map<DoubleHash,int,DoubleHashHasher> freq;
            freq.reserve(200000); // might help reduce rehashing
            freq.max_load_factor(0.7f);

            for(int i=0; i<n; i++){
                const auto &rhObj = rh[i];
                const auto &s = seq[i];
                unordered_set<DoubleHash, DoubleHashHasher> used;
                used.reserve(s.size());

                int limit = (int)s.size() - mid + 1;
                for(int start=0; start<limit; start++){
                    DoubleHash h = rhObj.getHash(start, mid);
                    used.insert(h);
                }
                for(auto &hashVal : used){
                    freq[hashVal]++;
                }
            }


            vector<DoubleHash> candidates;
            candidates.reserve(freq.size());
            for(auto &kv : freq){
                if(kv.second >= needed){
                    candidates.push_back(kv.first);
                }
            }

            if(!candidates.empty()){
                bestLen = mid;
                bestHashes = move(candidates);
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        if(bestLen == 0){
            cout << "?\n\n";
            continue;
        }

        unordered_set<DoubleHash, DoubleHashHasher> winningSet(
            bestHashes.begin(), bestHashes.end());
        

        set<string> finalSubs;

        for(int i=0; i<n; i++){
            const auto &rhObj = rh[i];
            const auto &s = seq[i];
            int limit = (int)s.size() - bestLen + 1;
            for(int start=0; start<limit; start++){
                DoubleHash h = rhObj.getHash(start, bestLen);
                if(winningSet.count(h)) {
                    finalSubs.insert(s.substr(start, bestLen));
                }
            }
        }

        for(const auto &sub : finalSubs){
            cout << sub << "\n";
        }
        cout << "\n";
    }

    return 0;
}