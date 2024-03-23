// 

class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> freq;
        for (int i = 0; i < s.length(); i++) {
            freq[s[i]] ++;
        }

        for (int j = 0; j < s.length(); j++) {
            if (freq[s[j]] == 1) {return j;}
        }

        return -1;
        
    }
};