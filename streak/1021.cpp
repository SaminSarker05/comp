#include <algorithm>

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int maxFreq = 0;
        // pass iterators marking start and end of container
        // return value is iterator as well
        auto maxValI = std::max_element(nums.begin(), nums.end());
        int maxVal = *maxValI + k + 1;  // dereference iteratior
        std::vector<int> prefix(maxVal, 0);

        // store the frequency of each number
        for (const int& num : nums) {
            prefix[num]++;
        }
        // create a prefix sum to calculate total cnt of numbers within a range
        for (int i = 1; i < maxVal; ++i) {
            prefix[i] += prefix[i - 1];
        }
        // each index i represents count of #'s <= i
        for (int i = 1; i < maxVal; i++) {
            int r = std::min(i + k, maxVal - 1);
            int l = std::max(i - k, 0);

            // total # of elements that can be converted to i
            int orig_freq = prefix[i] - prefix[i - 1];
            int possiblefreq = prefix[r] - (l > 0 ? prefix[l - 1] : 0);

            maxFreq = std::max(maxFreq, orig_freq + std::min(numOperations, possiblefreq - orig_freq));
        }
        return maxFreq;
    }
};

