#include <bits/stdc++.h>
using namespace std;

long long mod(long long a, long long m) {            // positive remainder
    return (a % m + m) % m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;                                            // number of scenarios
    if (!(cin >> n)) return 0;

    while (n--) {
        long long s11,s12,p11,p12;
        long long s21,s22,p21,p22;

        cin >> s11 >> s12 >> p11 >> p12;
        cin >> s21 >> s22 >> p21 >> p22;

        long long p = std::gcd(std::gcd(p11, p12),
                                std::gcd(p21, p22));

        long long t = mod(mod(s11, p) - mod(s12, p)
                         - mod(s21, p) + mod(s22, p), p);

        cout << (t == 0 ? "Yes" : "No") << '\n';
    }
    return 0;
}
