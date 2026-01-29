class Solution {
public:
    bool dfs(std::vector<int>& arr, int pos, int dir, int remain) {
        if (pos < 0 || pos >= arr.size()) {
            return remain == 0;
        }
        if (arr[pos] == 0) {
            return dfs(arr, pos + dir, dir, remain);
        }
        arr[pos] -= 1;
        dir *= -1;
        bool valid = dfs(arr, pos + dir, dir, remain - 1);
        arr[pos] += 1;
        return valid;
    }
    int countValidSelections(vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int res = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                if (dfs(nums, i, 1, total)) { res++; }
                if (dfs(nums, i, -1, total)) { res++; }
            }
        }
        return res;
    }
};

