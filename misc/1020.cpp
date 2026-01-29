class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;

        for (const std::string& s : operations) {
            // 2nd char can classify increment/decrement op
            if (s[1] == '+') { x++; }
            else { x--; }
        }
        return x;
    }
};
