class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> seen;

        for (int i = 0; i < strs.size(); i++) {
            string word = strs[i];
            sort(word.begin(), word.end());
            seen[word].push_back(strs[i]);
        }

        vector<vector<string>> res;
        for (auto const& [key, val] : seen) {
            res.push_back(val);
        }
        return res; 
    }
};