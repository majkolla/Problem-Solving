#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

/* ---------- prime sieve (√2^31 ≈ 46340) ---------- */
vector<int> build_primes() {
    const int LIM = 46350;
    vector<bool> is_prime(LIM + 1, true);
    vector<int> primes;
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= LIM; ++i)
        if (is_prime[i])
            for (int j = i * i; j <= LIM; j += i) is_prime[j] = false;
    for (int i = 2; i <= LIM; ++i)
        if (is_prime[i]) primes.push_back(i);
    return primes;
}

/* exponent of p in n! (Legendre) */
inline int64 vp_in_fact(int n, int p) {
    int64 cnt = 0;
    for (int64 power = p; power <= n; power *= p)
        cnt += n / power;
    return cnt;
}

bool divides_factorial(int n, int m, const vector<int>& primes) {
    if (m == 0) return false;          // 0 never divides
    if (m == 1) return true;           // 1 always divides
    if (n == 0) return m == 1;         // 0! = 1

    int tmp = m;
    for (int p : primes) {
        if (1LL * p * p > tmp) break;
        if (tmp % p == 0) {
            int need = 0;
            while (tmp % p == 0) { tmp /= p; ++need; }
            if (vp_in_fact(n, p) < need) return false;
        }
    }
    if (tmp > 1) { // remaining prime factor > √m
        if (vp_in_fact(n, tmp) < 1) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const vector<int> primes = build_primes();
    int n, m;
    while (cin >> n >> m) {
        if (divides_factorial(n, m, primes))
            cout << m << " divides " << n << "!\n";
        else
            cout << m << " does not divide " << n << "!\n";
    }
    return 0;
}
