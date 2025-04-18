#include <bits/stdc++.h>
using namespace std;

/*
we get the input: 
first line an integer that tells the number of data sets that is coming 
each data set consists of a single line of input. It contains the data set K
Followed by the happy prime candidate m 
*/

vector<bool> sieve_primes(int limit = 10000) {
    vector<bool> is_prime(limit + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= limit; ++p)
        if (is_prime[p])
            for (int i = p * p; i <= limit; i += p)
                is_prime[i] = false;
    return is_prime;
}

inline int digit_square_sum(int n) {
    int s = 0;
    while (n) {
        int d = n % 10;
        s += d * d;
        n /= 10;
    }
    return s;
}

bool is_happy(int n) {
    unordered_set<int> seen;
    while (n != 1 && !seen.count(n)) {
        seen.insert(n);
        n = digit_square_sum(n);
    }
    return n == 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const auto prime = sieve_primes();

    int P;                     
    if (!(cin >> P)) return 0;
    while (P--) {
        int K, m;               
        cin >> K >> m;
        bool happy_prime = prime[m] && is_happy(m);
        cout << K << ' ' << m << ' ' << (happy_prime ? "YES" : "NO") << '\n';
    }
    return 0;
}
