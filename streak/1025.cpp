class Solution {
public:
    int totalMoney(int n) {
        int total = 0;
        int start = 0;
        int curr = 0;

        for (int i = 1; i <= n; i++) {
            if (i % 7 == 1) {  // if monday increment start and reset
                start++;
                curr = start;
            }
            total += curr;
            curr++;
        }

        return total;
    }
};

