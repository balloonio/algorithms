/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* temp = node->next;
        node->val = temp->val;
        node->next = temp->next;
    }
};

/*
 Status: Accepted
 Runtime: 16 ms
 Submitted: 1 year ago
 You are here!
 Your runtime beats 19.74% of cpp submissions.
*/