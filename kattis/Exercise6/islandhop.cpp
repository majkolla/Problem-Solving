#include <bits/stdc++.h>
using namespace std;

struct UnionFind {
    vector<int> parent, rank_;
    UnionFind(int n) : parent(n), rank_(n, 0) {
        for(int i = 0; i < n; i++) parent[i] = i;
    }
    
    int findSet(int v) {
        if(parent[v] != v) parent[v] = findSet(parent[v]);
        return parent[v];
    }
    
    bool unionSet(int a, int b) {
        a = findSet(a), b = findSet(b);
        if(a == b) return false;
        if(rank_[a] < rank_[b]) swap(a, b);
        parent[b] = a;
        if(rank_[a] == rank_[b]) rank_[a]++;
        return true;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;  // number of test cases
    cin >> T;
    while(T--){
        int m; // number of islands
        cin >> m;
        
        vector<pair<double,double>> coords(m);
        for(int i = 0; i < m; i++){
            cin >> coords[i].first >> coords[i].second;
        }
        
        vector<tuple<double,int,int>> edges;
        edges.reserve((long long)m*(m-1)/2);  // safe reservation for up to m*(m-1)/2 edges
        
        for(int i = 0; i < m; i++){
            for(int j = i+1; j < m; j++){
                double dx = coords[i].first - coords[j].first;
                double dy = coords[i].second - coords[j].second;
                double dist = sqrt(dx*dx + dy*dy);
                edges.push_back({dist, i, j});
            }
        }
        
        sort(edges.begin(), edges.end(),
             [](auto &a, auto &b){
                 return get<0>(a) < get<0>(b);
             });
        
        UnionFind uf(m);
        double mst_length = 0.0;
        int edges_used = 0;
        
        for(auto &e : edges){
            double dist;
            int a, b;
            tie(dist, a, b) = e;
            if(uf.unionSet(a,b)){
                mst_length += dist;
                edges_used++;
                if(edges_used == m-1) break;
            }
        }
        
        cout << fixed << setprecision(6) << mst_length << "\n";
    }
    return 0;
}
