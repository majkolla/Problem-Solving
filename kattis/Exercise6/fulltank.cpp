#include <bits/stdc++.h>
using namespace std;

static const int INF = INT_MAX;

struct Edge {
    int to, w;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> fuelPrice(n);
    for(int i = 0; i < n; i++){
        cin >> fuelPrice[i];
    }

    vector<vector<Edge>> roads(n);
    for(int i = 0; i < m; i++){
        int u, v, d;
        cin >> u >> v >> d;
        roads[u].push_back({v, d});
        roads[v].push_back({u, d});
    }

    int q;
    cin >> q;
    while(q--){
        int C, s, e;
        cin >> C >> s >> e;

        vector<vector<int>> dist(n, vector<int>(C+1, INF));
        dist[s][0] = 0;   // Start at city s with 0 fuel and cost 0

        priority_queue< tuple<int,int,int>, vector<tuple<int,int,int>>, greater<> > pq;
        pq.push({0, s, 0});

        int answer = -1;

        while(!pq.empty()){
            auto [cost, city, fuel] = pq.top();
            pq.pop();
            
            // If this cost is outdated, skip
            if(cost > dist[city][fuel]) continue;

            // If we've reached city e, we can stop – this is the cheapest
            if(city == e){
                answer = cost;
                break;
            }

            // 1) Buy fuel (if possible)
            if(fuel < C){
                int newFuel = fuel + 1;
                int newCost = cost + fuelPrice[city];
                if(newCost < dist[city][newFuel]){
                    dist[city][newFuel] = newCost;
                    pq.push({newCost, city, newFuel});
                }
            }

            for(auto &edge : roads[city]){
                int nxt = edge.to, d = edge.w;
                if(d <= fuel){
                    int newFuel = fuel - d;
                    if(cost < dist[nxt][newFuel]){
                        dist[nxt][newFuel] = cost;
                        pq.push({cost, nxt, newFuel});
                    }
                }
            }
        }

        if(answer == -1) cout << "impossible\n";
        else cout << answer << "\n";
    }
    return 0;
}
