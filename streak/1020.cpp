class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;

        for (const std::string& s : operations) {
            // implicit conversion of string literal to std::string
            if (s == "++X" || s == "X++") {
                x++;
            } else {
                x--;
            }
        }
        return x;
    }
};

