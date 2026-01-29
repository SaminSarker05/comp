class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        std::vector<std::vector<int>> grid(m, std::vector<int>(n, 0));
        // 0 unwatched, 1 guard, 2 wall, 3 watched
        // do sweeps across the grid

        // mark guards and walls
        for (auto& g : guards) {
            grid[g[0]][g[1]] = 1;
        }
        for (auto& w : walls) {
            grid[w[0]][w[1]] = 2;
        }
        // left to right
        for (int i = 0; i < m; i++) {
            bool guard = false;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) { guard = true; } 
                else if (grid[i][j] == 2) { guard = false; }
                else if (guard) { grid[i][j] = 3; }
            }
        }
        // right to left
        for (int i = 0; i < m; i++) {
            bool guard = false;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) { guard = true; } 
                else if (grid[i][j] == 2) { guard = false; }
                else if (guard) { grid[i][j] = 3; }
            }
        }
        // top to bottom
        for (int j = 0; j < n; j++) {
            bool guard = false;
            for (int i = 0; i < m; i++) {
                if (grid[i][j] == 1) { guard = true; } 
                else if (grid[i][j] == 2) { guard = false; }
                else if (guard) { grid[i][j] = 3; }
            }
        }
        // bottom to top
        for (int j = 0; j < n; j++) {
            bool guard = false;
            for (int i = m - 1; i >= 0; i--) {
                if (grid[i][j] == 1) { guard = true; } 
                else if (grid[i][j] == 2) { guard = false; }
                else if (guard) { grid[i][j] = 3; }
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    res++;
                }
            }
        }

        return res;
    }
};

