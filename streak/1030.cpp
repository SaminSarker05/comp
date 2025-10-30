class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        int moves = 0;
        std::vector<int> increments(target.size(), 0);
        int prev = 0;
        
        for (int i = 0; i < target.size(); i++) {
            increments[i] = (target[i] - prev);
            prev = target[i];
        }
        for (const int& v : increments) {
            if (v > 0) { moves += v; }
        }

        return moves;
    }
};

