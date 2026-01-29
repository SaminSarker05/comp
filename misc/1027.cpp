class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int lasers = 0;
        int prev = 0;
        int curr = 0;

        for (const string& row : bank) {
            curr = 0;
            for (int i = 0; i < row.length(); i++) {
                if (row[i] == '1') { curr++; }
            }
            if (curr > 0) {
                lasers += (prev * curr);
                prev = curr;
            }
        }
        return lasers;
    }
};

