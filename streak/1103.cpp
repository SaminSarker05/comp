class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        std::stack<int> stack;
        int res = 0;

        for (int i = 0; i < colors.size(); i++) {
            if (stack.size() == 0 || colors[i] != colors[stack.top()]) {
                stack.push(i);
            } else {
                if (neededTime[i] <= neededTime[stack.top()]) {
                    res += neededTime[i];
                } else {
                    res += neededTime[stack.top()];
                    stack.pop();
                    stack.push(i);
                }
            }
        }
        return res;
    }
};

