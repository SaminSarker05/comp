class Solution {
public:
    bool hasSameDigits(string s) {
        string tmp = "";
        while (s.length() != 2) {
            tmp = "";
            for (int i = 1; i < s.length(); i++) {
                // operator+=(int) exists for std::string
                tmp += ((s[i] - '0') + (s[i - 1] - '0')) % 10;
            }
            s = tmp;
        }
        return s[0] == s[1];
    }
};

