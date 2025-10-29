class Solution {
public:
    int smallestNumber(int n) {
        int x = 1;
        while (x < n) {
            x <<= 1;
            x |= 1;
        }
        return x;
    }
};

