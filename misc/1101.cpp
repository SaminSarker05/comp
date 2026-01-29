/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        std::set<int> store(nums.begin(), nums.end());
        while (head && store.find(head->val) != store.end()) {
            head = head->next;
        }

        ListNode* newhead = head;
        ListNode* curr = head;
        
        while (curr) {
            ListNode* nexth = curr->next;
            while (nexth && store.find(nexth->val) != store.end()) {
                nexth = nexth->next;
            }
            curr->next = nexth;
            curr = nexth;
        }
        return newhead;
    }
};

