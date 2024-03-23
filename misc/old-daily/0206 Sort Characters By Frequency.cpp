class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;
        for (auto c : s) {
            freq[c] ++;
        }

        map<int, vector<char>> byval;
        for (auto const& [key, val] : freq) {
            byval[val].push_back(key);
        }

        vector<int> values;
        for (auto const& [key, val] : byval) {
            values.push_back(key);
        }
        
        string res = "";
        for (size_t i = values.size(); i > 0; i--) {
            int fre = values[i-1];
            for (char character : byval[fre]) {
                int temp = fre;
                while (temp) {
                    res += character;
                    temp --;
                }
            }
        }

        return res;
    }
};