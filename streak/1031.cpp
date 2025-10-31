class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        std::unordered_map<int, int> freqlist;
        for (const int& num : nums) {
            freqlist[num] += 1;
        }
        std::vector<int> res = {};
        for (auto item : freqlist) {
            if (item.second == 2) {
                res.push_back(item.first);
            }
        }
        return res;
    }
};

