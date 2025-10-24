class Solution {
public:
    bool compute(int x) {
        std::string sn = std::to_string(x);
        std::vector<int> store(10, 0);

        for (int i = 0; i < sn.length(); i++) {
            store[sn[i] - '0']++;
        }
        for (auto i : sn) {
            int digit = i - '0';
            if (digit != store[digit]) {
                return false;
            }
        }
        return true; 
    }
    int nextBeautifulNumber(int n) {
        n += 1;
        for (int i = n + 1; ;n++) {
            if (compute(n)) {
                return n;
            }
        }
        return -1;
    }
};

