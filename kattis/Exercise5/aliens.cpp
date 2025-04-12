#include <bits/stdc++.h>
using namespace std;

// We'll use simple 4-direction movement for BFS
static const int dx[4] = {1, 0, -1, 0};
static const int dy[4] = {0, 1, 0, -1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N; 
    cin >> N;
    
    while(N--){
        int x, y;
        cin >> x >> y;
        
        vector<string> maze(y);
        for(int i = 0; i < y; i++){
            cin >> maze[i];
        }
        vector<pair<int,int>> points;

        
        for(int r = 0; r < y; r++){
            for(int c = 0; c < x; c++){
                if(maze[r][c] == 'S'){
                    points.push_back({r,c});
                }
            }
        }
        
        for(int r = 0; r < y; r++){
            for(int c = 0; c < x; c++){
                if(maze[r][c] == 'A'){
                    points.push_back({r,c});
                }
            }
        }
        
        int k = (int)points.size(); 
        

        vector<vector<int>> dist(k, vector<int>(k, 0));
        
        auto bfs = [&](int index){
            vector<vector<int>> d(y, vector<int>(x, -1));
            queue<pair<int,int>>q;
            auto [sr, sc] = points[index];
            d[sr][sc] = 0;
            q.push({sr,sc});
            
            while(!q.empty()){
                auto [rr, cc] = q.front(); 
                q.pop();
                for(int i=0;i<4;i++){
                    int nr = rr + dy[i];
                    int nc = cc + dx[i];
                    if(nr<0||nr>=y||nc<0||nc>=x) continue;
                    if(maze[nr][nc] == '#') continue; 
                    if(d[nr][nc] == -1){ 
                        d[nr][nc] = d[rr][cc] + 1;
                        q.push({nr,nc});
                    }
                }
            }
            for(int j = 0; j < k; j++){
                auto [rr, cc] = points[j];
                dist[index][j] = d[rr][cc];
            }
        };
        
        for(int i = 0; i < k; i++){
            bfs(i);
        }
        
        
        struct Edge {
            int u, v, w;
        };
        vector<Edge> edges;
        edges.reserve(k*(k-1)/2);
        for(int i=0;i<k;i++){
            for(int j=i+1;j<k;j++){
                edges.push_back({i,j,dist[i][j]});
            }
        }
        sort(edges.begin(), edges.end(), [](auto &a, auto &b){
            return a.w < b.w;
        });
        
        vector<int> par(k), rankv(k,0);
        iota(par.begin(), par.end(), 0);
        
        function<int(int)> findp = [&](int v){
            return (par[v]==v)?v:par[v]=findp(par[v]);
        };
        
        auto unite = [&](int a, int b){
            a = findp(a); b = findp(b);
            if(a != b){
                if(rankv[a]<rankv[b]) swap(a,b);
                par[b] = a;
                if(rankv[a]==rankv[b]) rankv[a]++;
                return true;
            }
            return false;
        };
        
        long long mstCost = 0;
        int edgesUsed = 0;
        for(auto &e : edges){
            if(unite(e.u, e.v)){
                mstCost += e.w;
                edgesUsed++;
                if(edgesUsed == k-1) break;
            }
        }
        
        cout << mstCost << "\n";
    }
    
    return 0;
}
